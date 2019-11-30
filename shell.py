# Mini-c shell
# For executing c-code that already be parsed by parser
# Some simple debugging (ex. print, next, continue, kill)
# By 2019F CS420 Team 4

import sys
import string


# executing code on shell
def run (file_name):
    # init : open code and create class for code
    code = Executing_code(file_name)
    # if not opened, return and retry
    if code.file == None: return

    # compile
    try:
        code.compile()
    except:
        print("Compile Error")
        code.file.close()
        return

    # run code
    while True:
        command = input()
        cmd_parse = [x for x in command.split(' ') if x.strip()]
        cmd = cmd_parse[0]
        if cmd == "c" or cmd == "continue" : code.continue_code()
        elif cmd == "q" or cmd == "quit":
            code.file.close()
            return
        elif len(cmd_parse) == 2:
            if cmd == "n" or cmd == "next": code.next(cmd_parse[1])
            elif cmd == "p" or cmd == "print": code.print_var(cmd_parse[1])
            elif cmd == "t" or cmd == "trace": code.trace_var(cmd_parse[1])
            else: print("wrong command on shell")
        else: print("wrong command on shell")



class Executing_code:
    def __init__(self, file_name):
        self.file = None
        try:
            self.file = open(file_name)
        except:
            print("Not exist file named " + '\"' + file_name + '\"')
        print("file open succecced")
        self.sym_table = None
        self.parse_tree = None
        self. cur_var_table = {}
        self.cur_line = 1

    def compile(self):
        # get symbol table
        # get parse tree?
        # by using try except
        return

    def continue_code(self):
        return

    def next(self, line_num):
        if self.cur_line >= line_num:
            print("wrong command on shell")
            return
        while self.cur_line != line_num: self.next_line()
        return

    def next_line(self):
        # if iterate,
        # do something!

        # else, go to next line
        self.cur_line += 1

        return

    def print_var(self, var):
        return

    def trace_var(self, var):
        return


# main
def shell():
    while (True):
        command = input()

        # exit shell
        if command == "q" or command == "quit" : return
        else:
            cmd_parse = [x for x in command.split(' ') if x.strip()]
            cmd = cmd_parse[0]

            # try to run code on shell
            if cmd == "run" and len(cmd_parse) == 2: run(cmd_parse[1])
            else: print("wrong command")

shell()