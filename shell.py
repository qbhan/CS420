# Mini-c shell
# Some simple debugging (ex. print, next, continue, kill)
# By 2019F CS420 Team 4

import sys
import string


from datastructure import *
from pycvisitor import *
from ply import yacc as yacc
from pycparser import *
from pyclexer import *
import globalVar
import threading
import time

# executing code on shell
def run (file_name):
    # init : open code and create class for code
    code = Executing_code(file_name)
    # if not opened, return and retry
    if code.file is None:
        return

    # compile
    try:
        code.compile()
    except:
        print("Compile Error")
        code.file.close()
        return

    globalVar.lock.acquire()
    execute = threading.Thread(target = Visitor.visit_interp, args = (code.interp_visitor, code.ast))
    execute.start()

    # run code
    while True:
        command = input("System) CLI command : ")
        cmd_parse = [x for x in command.split(' ') if x.strip()]
        if len(cmd_parse)< 1:
            print("System) wrong command")
            continue

        cmd = cmd_parse[0]
        if cmd == "c" or cmd == "continue":
            globalVar.lineno_diff = "continue"
            code.continue_code()
            globalVar.lock.release()
            break
        elif cmd == "q" or cmd == "quit":
            code.file.close()
            print("\nQuit current execution\n\n")
            return
        elif len(cmd_parse) == 2:
            if cmd == "n" or cmd == "next":
                if int(cmd_parse[1]) <= 0:
                    print("line number should be larger than 0")
                    continue
                globalVar.lineno_diff = int(cmd_parse[1])
                code.continue_code()
                if not execute.is_alive():
                    break

            elif cmd == "p" or cmd == "print": code.print_var(cmd_parse[1])
            elif cmd == "t" or cmd == "trace": code.trace_var(cmd_parse[1])
            else: print("wrong command on shell")
        else: print("wrong command on shell")
    execute.join()
    print(execute)


class Executing_code:
    def __init__(self, file_name):
        global lineno_diff
        self.file = None
        try:
            self.file = open(file_name, 'r')
        except:
            print("Not exist file named " + '\"' + file_name + '\"')
        else:
            print("file open succeeded")
            self.symtab_visitor = SymtabVisitor()
            self.interp_visitor = InterpVisitor()
            self.parser = None
            self.ast = None
            self.cur_line = 0
            self.codelist = []

    def compile(self):
        self.parser = yacc.yacc()
        input = ""
        globalVar.codelist = []
        while True:
            line = self.file.readline()
            globalVar.codelist.append(line)
            input += line
            if not line:
                break
        self.file.close()
        lexer = lex.lex()
        self.ast = self.parser.parse(input)
        # self.symtab_visitor.visit_symtab(self.ast)

        # if error handling succeed, then raise error => depend on global variable, which will be added later

    def continue_code(self):
        globalVar.lock.release()
        time.sleep(0.1)
        globalVar.lock.acquire()


    def print_var(self, var):
        if '*' not in var and '[' not in var:
            # case ID
            history = self.interp_visitor.currSymtab.get_history(var)
            if history is not None:
                try:
                    p = history[-1][0]
                    print('\t'+ var + ' :', p)
                except:
                    print("System) Not assigned yet.")
        elif '[' not in var:
            # case referencing pointer
            if len(var) < 2 and var[0] != '*':
                print("System) wrong args in print.")
                return
            ptr = var[1: len(var)]
            history = self.interp_visitor.currSymtab.get_history(ptr)
            if history is not None:
                addr = history[-1][0]
                try:
                    print ('\t'+ var + ' :', self.interp_visitor.memory[addr][-1][0])
                except:
                    print("System) Not assigned yet.")
        elif '*' not in var:
            # case normal array entry
            il = var.index('[')
            ir = var.index(']')
            idx = int(var[il+1:ir])
            array = var[:il]
            history = self.interp_visitor.currSymtab.get_history(array)
            if history is not None:
                addr = history[-1][0]
                try:
                    print('\t' + var + ' :', self.interp_visitor.memory[addr+idx][-1][0])
                except:
                    print("System) Not assigned yet.")
            else:
                print("System) wrong args in print.")

        else:
            il = var.index('[')
            ir = var.index(']')
            idx = int(var[il + 1:ir])
            array = var[1:il]
            history = self.interp_visitor.currSymtab.get_history(array)
            if history is not None:
                addr = history[-1][0]
                ptr = self.interp_visitor.memory[addr + idx][-1][0]
                try:
                    print('\t' + var + ' :', self.interp_visitor.memory[ptr][-1][0])
                except:
                    print("System) Not assigned yet.")
            else:
                print("System) wrong args in print.")

    def trace_var(self, var):
        if '*' not in var and '[' not in var:
            # case ID
            history = self.interp_visitor.currSymtab.get_history(var)
            if history:
                print('\t'+ var + ' history :', self.interp_visitor.currSymtab.get_history(var))
        elif '[' not in var:
            # case referencing pointer
            if len(var) < 2 and var[0] != '*':
                print("System) wrong args in trace.")
                return
            ptr = var[1: len(var)]
            history = self.interp_visitor.currSymtab.get_history(ptr)
            if history:
                addr = history[-1][0]
                print (self.interp_visitor.memory[addr])
        elif '*' not in var:
            # case normal array entry
            il = var.index('[')
            ir = var.index(']')
            idx = int(var[il + 1:ir])
            array = var[:il]
            history = self.interp_visitor.currSymtab.get_history(array)
            if history:
                addr = history[-1][0]
                print(self.interp_visitor.memory[addr + idx])
            else:
                print("System) wrong args in trace.")
        else:
            il = var.index('[')
            ir = var.index(']')
            idx = int(var[il + 1:ir])
            array = var[1:il]
            history = self.interp_visitor.currSymtab.get_history(array)
            if history is not None:
                addr = history[-1][0]
                ptr = self.interp_visitor.memory[addr + idx][-1][0]
                try:
                    print('\t' + var + ' :', self.interp_visitor.memory[ptr])
                except:
                    print("System) Not assigned yet.")
            else:
                print("System) wrong args in trace.")



# main
def shell():
    while (True):
        command = input("command on shell : ")
        if (len(command) < 1):
            print("wrong command")
            continue
        # exit shell
        if command == "q" or command == "quit" :
            print("Close shell...")
            return
        else:
            cmd_parse = [x for x in command.split(' ') if x.strip()]
            cmd = cmd_parse[0]

            # try to run code on shell
            if cmd == "run" and len(cmd_parse) == 2:
                print("Execute "+ cmd_parse[1] + "...")
                run(cmd_parse[1])
            else: print("System) wrong command")

shell()