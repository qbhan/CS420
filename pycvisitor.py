from datastructure import *

class Visitor:

    def __init__(self):
        self.message = "BASIC VISITOR"

    def visit_symtab(self, node):
        return node.accept(self)

    def visit_interp(self, node):
        return node.interp(self)

class Symtab:

    def __init__(self, parent=None):

        # {name : [(value, lineno)...]}
        self.history = {}
        self.entry = {}
        self.parent = parent
        if self.parent:
            self.parent.children.append(self)
        self.children = []

    def add(self, name, value):
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


class SymtabVisitor(Visitor):

    def __init__(self):
        Visitor.__init__(self)
        self.message = "SYMBOL TABLE VISITOR"
        # TODO make current symbol table

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
        if node.name in entry:
            print("Error : Cannot declare same identifier twice.")
        else:
            self.currSymtab.add(node.name, node)

    # Assigning a value to the identifier. e.g. a = x + 3;
    def sAssignment(self, node):
        node.id.accept(self)
        node.value.accept(self)
        id_name = node.id.name
        symbol_value = self.currSymtab.get(node.id.name)
        if symbol_value is None:
            print("Error : The assignment of", id_name, "at line", node.id.lineno, "is not declared.")
        else:
            self.currSymtab.add(id_name, node)

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

    def sBinop(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def sIf(self, node):
        self.NewSymTab(node)
        node.cond_stmt.accept(self)
        node.body.accept(self)
        node.else_body.accept(self)
        self.PopSymTab(node)

    def sFor(self, node):
        self.NewSymTab(node)
        node.init_stmt.accept(self)
        node.cond_stmt.accept(self)
        node.incr_stmt.accept(self)
        node.body.accept(self)
        self.PopSymTab(node)

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

    def sStmtList(self, node):
        return self.sNodeList(node)

    # 5. Function issues
    # Function definitions e.g. int f(float x){ float y = 1; return x+y; }.
    def sFunction(self, node):
        self.currSymtab.add(node.name, node)
        self.NewSymTab(node)
        node.param_list.accept(self)
        errorprone = node.body.accept(self)
        if node.type is not 'void':
            if not errorprone == 'ReturnStmt':
                print("Error : There is no Return Statement.")
        self.PopSymTab(node)

    # Function expressions e.g. f(1.0)
    def sFunctionCall(self, node):
        node.function.accept(self)
        node.arglist.accept(self)

    # Parameter List for function definitions.
    def sParameterList(self, node):
        for item in node.nodes:
            item.accept(self)
            self.currSymtab.add(item.name, item)



class InterpVisitor(Visitor):

    def __init__(self):
        Visitor.__init__(self)
        self.message = "Interpreter VISITOR"

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

    def iNodeList(self, node):
        list = node.nodes
        print(node.nodes)
        res = []
        for ast in list:
            res.append(ast.interp(self))
        return res

    def iIdentifier(self, node):
        return self.currSymtab.history[node.name][-1][0]

    def iDeclStmt(self, node):
        self.currSymtab.add(node.name, node)
        self.currSymtab.history[node.name] = []

    def iAssignment(self, node):
        self.currSymtab.history[node.id.name].append((node.value.interp(self), node.id.lineno))

    def iConstant(self, node):
        return node.value

    def iNegation(self, node):
        return (-1) * node.expr.interp(self)

    def iIncrement(self, node):

        # Dive down deeply but not too far or you'll get drown...
        if node.is_prefix:
            val = node.expr.interp(self)+1
            self.currSymtab.history[node.expr.name].append((val, node.lineno))
        else:
            val = node.expr.interp(self)
            self.currSymtab.history[node.expr.name].append((val+1, node.lineno))
        return val

    def iBinop(self, node):
        l = node.left.interp(self)
        r = node.right.interp(self)
        if l and r:
            return eval(str(l) + node.binop + str(r))
        else:
            print("Error : Binary operation error")
            return None

    def iReturnStmt(self, node):
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
        function = node.function
        parameters = function.param_list.nodes # List of DeclStmt Nodes
        for i in range(len(arguments)):
            arg = arguments[i]
            par = parameters[i]
            node.function.symtab.history[par.name].append((arg, 99999999))
        res = function.body.interp(self)
        for i in range(len(arguments)):
            par = parameters[i]
            node.function.symtab.history[par.name] = []
        return res

    def iStmtList(self, node):
        list = node.nodes
        res = None
        for ast in list:
            res = ast.interp(self)
        return res


    def iFor(self, node):
        pass