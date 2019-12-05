from datastructure import *

class Visitor:

    def __init__(self):
        self.message = "BASIC VISITOR"

    def visit(self, node):
        return node.accept(self)

    def _visitList(self, list):
        res = None
        for ast in list:
            pivot = ast.accept(self)
        return res

class Symtab:
    pass

class SymtabVisitor(Visitor):

    def __init__(self):
        self.message = "SYMBOL TABLE VISITOR"

    # 0. Basic classes for defining symbol table visitor.
    # Base class for all ast nodes.
    def Node(self, node):
        pass

    # Push new symbol table to the stack.
    def NewSymTab(self, node):
        pass

    # Pop out the symbol table from the stack.
    # Whenever the scope it exited and discarded.
    def PopSymTab(self, node):
        pass

    # Put the node into the current symbol table, as a symbol.
    def PutSymbol(self, node):
        # TODO define lexScope, the current symbol table.
        # TODO fix (node.name, node) into something that contains history.
        self.lexScope.add(node.name, node)

    # 1. Implement after implementing push, pop and add symbol of symbol table.
    # Id. e.g. int a;.
    # "node.lineno" have to contain the line number value.
    def Identifier(self, node):
        pass

    # Declaration of an identifier. e.g. a = 1;.
    # Q. I think it might contain the line no value... does it?
    # Just add the symbol to the right key in the table.
    def Declstmt(self, node):
        pass

    # Function definitions e.g. int f(float x){ float y = 1; return x+y; }.
    def Function(self, node):
        pass

    # Array definitions e.g. int A[10];.
    def Array(self, node):
        pass

    # A compound statement, e.g. { int i; i += 1; }.
    def CompoundStmt(self, node):
        pass

    # 2. Easy cases/ Not related directly w/ symbol table.
    # Array expressions e.g. A[x+1].
    def Array_Index(self, node):
        node.name.accept(self)
        node.index.accept(self)

    # Function expressions e.g. f(1.0)
    def FunctionCall(self, node):
        node.function.accept(self)
        node.arglist.accept(self)

    # Including Negation, GetValue and GetAddress.
    def Unaryop(self, node):
        node.expr.accept(self)

    def Binop(self, node):
        node.left.accept(self)
        node.right.accept(self)

    def If(self, node):
        node.cond_stmt.accept(self)
        node.body.accept(self)
        node.else_body.accept(self)

    def For(self, node):
        node.init_stmt.accept(self)
        node.cond_stmt.accept(self)
        node.incr_stmt.accept(self)
        node.body.accept(self)

    def ReturnStmt(self, node):
        node.expr.accept(self)