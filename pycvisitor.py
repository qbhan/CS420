from datastructure import *
import globalVar
import sys

class Visitor:

    def __init__(self):
        self.message = "BASIC VISITOR"

    def visit_symtab(self, node):
        return node.accept(self)

    def visit_interp(self, node):
        globalVar.lock.acquire()
        ret = node.interp(self)
        globalVar.lock.release()
        print("\nSystem) execute finished\n\n")
        return ret

    # def visit_interp(self, node):
    #     return node.interp(self)

class Symtab:

    def __init__(self, parent=None):

        # {name : [(value, lineno)...]}
        self.history = {}
        self.entry = {}
        self.parent = parent
        if self.parent:
            self.parent.children.append(self)
        self.children = []

    def add_recursive(self,name, value):
        if name in self.entry:
            self.entry[name] = value
            return True
        if self.parent:
            return self.parent.add_recursive(name,value)
        else: return False

    def add(self, name, value):
        if not self.add_recursive(name,value):
            self.entry[name] = value



    def get(self, name):
        if name in self.entry:
            return self.entry[name]
        else:
            if self.parent:
                return self.parent.get(name)
            else:
                print("Error : Cannot find a key", name, "in all Symbol Table.")
                return None

    def get_history(self, name):
        if name in self.history:
            return self.history[name]
        else:
            if self.parent:
                return self.parent.get_history(name)
            else:
                print("Error : Cannot find a key", name, "in all Symbol Table.")
                return None

    def history_update(self, name, value):
        if name in self.history:
            # value is a tuple.
            self.history[name].append(value)
        else:
            if self.parent:
                return self.parent.history_update(name, value)
            else:
                print("Error : Cannot find a key", name, "in all Symbol Table.")
                return None

class SymtabVisitor(Visitor):

    def __init__(self):
        Visitor.__init__(self)
        self.message = "SYMBOL TABLE VISITOR"

    # 0. Basic classes for defining symbol table visitor.
    # Base class for all ast nodes.
    def sNode(self, node):
        pass

    # Push new symbol table to the stack.
    def NewSymTab(self, node):
        self.currSymtab = Symtab(self.currSymtab)

    # Pop out the symbol table from the stack.
    # Whenever the scope it exited and discarded.
    def PopSymTab(self, node):
        node.symtab = self.currSymtab
        self.currSymtab = self.currSymtab.parent

    # 1. Implement after implementing push, pop and add symbol of symbol table.
    # Just an identifier e.g. a, b, c ...
    # "node.lineno" have to contain the line number value.
    def sIdentifier(self, node):
        pass

    # Constant e.g. 3.
    def sConstant(self, node):
        pass

    # Declaration of an identifier. e.g. int a;.
    # Q. I think it might contain the line no value... does it?
    # Just add the symbol to the right key in the table.
    def sDeclStmt(self, node):
        entry = self.currSymtab.entry
        if node.name.name in entry:
            print("Error : Cannot declare same identifier twice.")
        else:
            assert (node.name.__class__.__name__ == 'Identifier')
            if node.type.__class__.__name__ == 'PointerType':
                self.curr_ptr += 1
            elif node.type.__class__.__name__ == 'ArrayType':
                self.curr_ptr += node.type.length
            else:
                pass
            self.currSymtab.add(node.name.name, node)

    # Assigning a value to the identifier. e.g. a = x + 3;
    def sAssignment(self, node):
        assign = node.id.__class__.__name__
        if assign == 'Identifier':
            node.id.accept(self)
            node.value.accept(self)
            id_name = node.id.name
            symbol_value = self.currSymtab.get(node.id.name)
            if symbol_value is None:
                print("Error : The assignment of", id_name, "at line", node.id.lineno, "is not declared.")
            else:
                self.currSymtab.add(id_name, node)
        elif assign == 'Pointer':
            pass
        elif assign == 'Array_index':
            pass
        else:
            print("Error : LHS has to be an identifier, a pointer or an array.")

    # Array definitions e.g. int A[10];.
    def sArray(self, node):
        pass

    def sReturnStmt(self, node):
        node.expr.accept(self)
        return 'ReturnStmt'

    # 2. Easy cases/ Not related directly w/ symbol table.
    # Array expressions e.g. A[x+1].
    def sArray_Index(self, node):
        node.name.accept(self)
        node.index.accept(self)

    # Including Negation, GetValue and GetAddress.
    def sUnary(self, node):
        node.expr.accept(self)

    def sIncrement(self, node):
        expression = self.currSymtab.entry.get(node.expr)
        if expression:
            expression.accept(self)
        else:
            print("Error : Cannot find the expression in Increment.")

    def sBinop(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def sIf(self, node):
        self.NewSymTab(node)
        node.cond_stmt.accept(self)
        res_body = node.body.accept(self)
        if node.else_body:
            res_else_body = node.else_body.accept(self)
        self.PopSymTab(node)
        if node.else_body:
            return (res_body and res_else_body)
        else:
            return res_body

    def sFor(self, node):
        self.NewSymTab(node)
        node.init_stmt.accept(self)
        node.cond_stmt.accept(self)
        node.incr_stmt.accept(self)
        res = node.body.accept(self)
        self.PopSymTab(node)
        return res

    # 4. Subclasses of NodeList.
    # Compiling the whole program.
    def sGlobalList(self, node):
        self.root = Symtab()
        self.currSymtab = self.root
        self.sNodeList(node)
        node.symtab = self.root

    def sNodeList(self, node):
        list = node.nodes
        res = None
        for ast in list:
            res = ast.accept(self)
        return res

    def sDeclStmtList(self, node):
        list = node.nodes
        res = None
        for ast in range(1, len(list)):
            res = list[ast].accept(self)
        return res

    def sStmtList(self, node):
        return self.sNodeList(node)

    # 5. Function issues
    # Function definitions e.g. int f(float x){ float y = 1; return x+y; }.
    def sFunction(self, node):
        self.currSymtab.add(node.name, node)
        self.NewSymTab(node)
        node.param_list.accept(self)
        # errorprone = node.body.accept(self)
        # if node.type is not 'void':
        #     if not errorprone == 'ReturnStmt':
        #         print("Error : There is no Return Statement.")
        self.PopSymTab(node)

    # Function expressions e.g. f(1.0)
    def sFunctionCall(self, node):
        # node.function is string, so we should lookup symboltable to find function node
        func = self.currSymtab.get(node.function)
        func.accept(self)
        node.arglist.accept(self)

    # Parameter List for function definitions.
    def sParameterList(self, node):
        for item in node.nodes:
            item.accept(self)
            self.currSymtab.add(item.name, item)



class InterpVisitor(Visitor):

    def __init__(self):
        Visitor.__init__(self)
        self.memory = [[] for i in range(100000)]
        self.curr_ptr = 0
        self.message = "Interpreter VISITOR"
        self.curr_lineno = 0

    # Push new symbol table to the stack.
    def NewSymTab(self, node):
        self.currSymtab = Symtab(self.currSymtab)

    # Pop out the symbol table from the stack.
    # Whenever the scope it exited and discarded.
    def PopSymTab(self, node):
        node.symtab = self.currSymtab
        self.currSymtab = self.currSymtab.parent

    def iNode(self, node):
        pass

    def iGlobalList(self, node):
        self.root = Symtab()
        self.currSymtab = self.root
        self.iNodeList(node)
        node.symtab = self.root

    def iDeclStmtList(self,node):
        list = node.nodes
        res = []
        for i in range(1, len(list)):
            res.append(list[i].interp(self))
        return res

    def iNodeList(self, node):
        list = node.nodes
        res = []
        for ast in list:
            res.append(ast.interp(self))
        return res

    def iIdentifier(self, node):
        history = self.currSymtab.get_history(node.name)
        return history[-1][0]

    def iPointer(self, node):
        if type(node.id) is str:
            history = self.currSymtab.get_history(node.id)
            addr = history[-1][0]
        else:
            addr = node.id.interp(self)
        if len(self.memory[addr]) != 0:
            return self.memory[addr][-1][0]
        else:
            return None


    def iArray_index(self, node):
        array = self.currSymtab.get(node.name)
        idx = node.index.interp(self)
        if array.type.__class__.__name__ == 'ArrayType' and array.type.length - 1 < idx:
            print("Segmentation fault : index out of range error")
            globalVar.lock.release()
            sys.exit()
        addr = self.currSymtab.get_history(node.name)[-1][0]
        return self.memory[addr + idx][-1][0]

    def iDeclStmt(self, node):
        assert (node.name.__class__.__name__ == 'Identifier')
        if node.type.__class__.__name__ == 'PointerType':
            self.currSymtab.history[node.name.name] = [(self.curr_ptr, node.lineno)]
            self.curr_ptr += 1
        elif node.type.__class__.__name__ == 'ArrayType':
            self.currSymtab.history[node.name.name] = [(self.curr_ptr, node.lineno)]
            if node.type.type.__class__.__name__ == 'PointerType':
                for i in range(node.type.length):
                    self.memory[self.curr_ptr] = [(self.curr_ptr + node.type.length, node.lineno)]
                    self.curr_ptr += 1
            self.curr_ptr += node.type.length
        else:
            self.currSymtab.history[node.name.name] = []
        self.currSymtab.add(node.name.name, node)


    def iAssignment(self, node):
        assign = node.id.__class__.__name__
        if assign == 'Identifier':
            self.currSymtab.history_update(node.id.name, (node.value.interp(self), node.id.lineno))
            # self.currSymtab.add(node.id.name, node)
        elif assign == 'Pointer':
            if node.id.id.__class__.__name__ == "Array_index":
                array = self.currSymtab.get(node.id.id.name)
                idx = node.id.id.index.interp(self)
                if array.type.length - 1 < idx:
                    print("Segmentation fault : index out of range error")
                    globalVar.lock.release()
                    sys.exit()
                array_addr = self.currSymtab.get_history(node.id.id.name)[-1][0]
                addr = self.memory[array_addr + idx][-1][0]
            else:
                addr = self.currSymtab.get_history(node.id.id)[-1][0]
            self.memory[addr].append((node.value.interp(self), node.lineno))
        elif assign == 'Array_index':
            array = self.currSymtab.get(node.id.name)
            idx = node.id.index.interp(self)
            if array.type.length - 1 < idx:
                print("Segmentation fault : index out of range error")
                globalVar.lock.release()
                sys.exit()

            addr = self.currSymtab.get_history(node.id.name)[-1][0]
            self.memory[addr + node.id.index.interp(self)].append((node.value.interp(self), node.lineno))
        else:
            print("Error : something wrong!")
            globalVar.lock.release()
            sys.exit()

    def iConstant(self, node):
        return node.value

    def iNegation(self, node):
        return (-1) * node.expr.interp(self)

    def iIncrement(self, node):
        id = Identifier(node.expr, node.lineno)
        # Dive down deeply but not too far or you'll get drown...
        if node.is_prefix:
            val = id.interp(self)+1
            self.currSymtab.history_update(node.expr, (val, node.lineno))
        else:
            val = id.interp(self)
            self.currSymtab.history_update(node.expr, (val+1, node.lineno))
        return val

    def iBinop(self, node):
        l = node.left.interp(self)
        r = node.right.interp(self)
        if l is not None and r is not None:
            return eval(str(l) + node.binop + str(r))
        else:
            print("Error : Binary operation error")
            globalVar.lock.release()
            sys.exit()

    def iReturnStmt(self, node):
        node.is_return = True
        return node.expr.interp(self)

    def iFunction(self, node):
        self.currSymtab.add(node.name, node)
        self.NewSymTab(node)
        node.param_list.interp(self)
        if node.name is 'main':
            node.body.interp(self)
        self.PopSymTab(node)

    def iParameterList(self, node):
        for item in node.nodes:
            item.interp(self)
            self.currSymtab.add(item.name, item)

    # TODO when datastructure's function call has an attribute lineno, 99999999->lineno
    def iFunctionCall(self, node):
        arguments = node.arglist.interp(self)
        self.NewSymTab(node)
        func = self.currSymtab.get(node.function)
        self.currSymtab.history = func.symtab.history
        self.currSymtab.entry = func.symtab.entry
        parameters = func.param_list.nodes # List of DeclStmt Nodes
        for i in range(len(arguments)):
            arg = arguments[i]
            par = parameters[i]
            self.currSymtab.history_update(par.name.name, (arg, node.lineno))

        res = func.body.interp(self)

        if not func.body.is_return:
            print("Error : no return statement in function call")
            globalVar.lock.release()
            sys.exit()

        for i in range(len(arguments)):
            par = parameters[i]
            #self.currSymtab.history[par.name.name] = []
        self.PopSymTab(node)
        return res

    def iStmtList(self, node):
        node.is_return = False
        list = node.nodes
        res = None
        for ast in list:
            res = ast.interp(self)
            if ast.is_return:
                node.is_return = True
                break
        return res


    def iFor(self, node):
        node.init_stmt.interp(self)
        self.NewSymTab(node)
        node.is_return = False
        while True:
            cond = node.cond_stmt.interp(self)
            if not cond:
                self.PopSymTab(node)
                return
            res = node.body.interp(self)
            node.is_return = node.body.is_return
            if node.is_return:
                self.PopSymTab(node)
                return res
            node.incr_stmt.interp(self)

    def iIf(self, node):
        self.NewSymTab(node)
        cond = node.cond_stmt.interp(self)
        is_ret = False;
        res = None
        if cond:
            res = node.body.interp(self)
            is_ret = node.body.is_return
        elif node.else_body:
            res = node.else_body.interp(self)
            is_ret = node.else_body.is_return
        node.is_return = is_ret
        self.PopSymTab(node)
        return res


    def iPrintf(self, node):
        list = node.arguments.nodes
        if len(list) == 1:
            s = list[0].value[1:-1]
            i = 0
            while i < len(s):
                if s[i] == '\\' and s[i + 1] == 'n':
                    print()
                    i += 2
                    continue
                print(s[i], end='')
                i += 1
            return
        else:
            def interpret(node):
                return node.interp(self)

            args = list[1:]
            interpreted_args = tuple(map(interpret, args))
            try:
                s = list[0].value[1:-1] % interpreted_args
                i = 0
                while i < len(s):
                    if s[i] == '\\' and s[i + 1] == 'n':
                        print()
                        i += 2
                        continue
                    print(s[i], end='')
                    i += 1
            except:
                print('Error : print format error in run time.')
                globalVar.lock.release()
                sys.exit()
