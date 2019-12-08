# TODO should implement array for memory
# TODO should make attibute of memory for classes
# TODO should make attibute of line number for classes for
#  line-by-line interpretation.
# TODO should make class for assignment.
# TODO Updating and changing symbol table should be done here.
#  Each class will have evaluate(). Should update and use symbol table here for
#  line-by-line interpretation.


# class Memory:
#     def __init__(self):
#         self.memory = []
#
#     def getValue(self, index):
#         if index < len(self.memory) - 1:
#             return self.memory[index]
#         else:
#             return None
#
#     def getAddress(self, value):
#         return self.memory.index(value)


class Null:
    def __init__(self):
        self.type = 'void'

    # def is_null(self):
    #     return True


# class Type:
#     def __init__(self, type):
#         self.type = type


class PointerType:
    def __init__(self, type):
        self.type = type

# TODO still dunno usage of function type
# class FunctionType:
#     def __init__(self, functype):
#         self.functype = functype

class Node():

    def accept(self, visitor):
        print("\n\nIN ACCEPT\nvisitor is", visitor)
        return self._accept(self.__class__, visitor)

    def _accept(self, klass, visitor):
        print("\n\nIN _ACCEPT\nklass is", klass.__name__, "\nvisitor is", visitor)
        visitor_method = getattr(visitor, "s%s" % klass.__name__, None)
        print(visitor_method)
        if visitor_method is None:
            if klass.__name__ == 'object':
                print("It's an object class.")
                return
            else:
                print("It's a subclass of Unary or NodeList.")
                base = klass.__bases__
                return self._accept(base[0], visitor)
        else:
            print("It's an attribute in SymtabVisitor.")
            return visitor_method(self)

    def interp(self, visitor):
        print("\n\nIN ACCEPT\nvisitor is", visitor)
        return self._interp(self.__class__, visitor)

    def _interp(self, klass, visitor):
        print("\n\nIN _ACCEPT\nklass is", klass.__name__, "\nvisitor is", visitor)
        visitor_method = getattr(visitor, "i%s" % klass.__name__, None)
        print(visitor_method)
        if visitor_method is None:
            if klass.__name__ == 'object':
                print("It's an object class.")
                return
            else:
                print("It's a subclass of Unary or NodeList.")
                base = klass.__bases__
                return self._accept(base[0], visitor)
        else:
            print("It's an attribute in InterpVisitor.")
            return visitor_method(self)


class Unary(Node):

    def __init__(self, node):
        self.expr = node
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class Negation(Unary):

    def evaluate(self):
        return -self.expr.evaluate()


class GetValue(Unary):
    # get value a from *a
    pass

    # need to make memory
    # def evaluate(self):
    #     return memory[self.expr.evaluate()]


class GetAddress(Unary):
    # get value a from &a
    pass

    # def evaluate(self):
    #     return memory.index(self.expr.evaluate)


class Increment(Unary):
    def __init__(self, expr, delay):
        self.expr = expr
        self.delay = delay

    def evaluate(self):
        return self.expr.evaluate() + 1


class ReturnStmt(Node):

    def __init__(self, expr):
        self.expr = expr
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class StmtBlock(Node):
    def __init__(self, stmt_list, sym_table):
        self.stmt_list = stmt_list
        self.sym_table = sym_table
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class FunctionCall(Node):
    def __init__(self, function, arglist):
        self.function = function
        self.arglist = arglist
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class Constant(Node):
    def __init__(self, value):
        self.type = type(value).__name__
        self.value = value
        self.lineno = None

    # def is_const(self):
    #     return True
    def setlineno(self, n):
        self.lineno = n

    def evaluate(self):
        return self.value

##########################################################################
# Made for string literals for printf usage.
##########################################################################
class Literal(Node):
    def __init__(self, literal):
        self.value = literal
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class Identifier(Node):
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

    def is_id(self):
        return True

    def setlineno(self, n):
        self.lineno = n


class Pointer(Node):
    def __init__(self, id):
        self.id = id
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


##########################################################################
# Address : For cases like &a
##########################################################################
class Address(Node):
    def __init__(self, value):
        self.value = value
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class Array(Node):
    def __init__(self, name, length):
        self.type = None
        self.name = name
        self.length = length
        self.lineno = None

    def settype(self, type):
        self.type = type

    def setlineno(self, n):
        self.lineno = n


class Array_index(Node):
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class Function(Node):
    def __init__(self, type, name, param_list, body):
        self.type = type
        self.name = name
        self.param_list = param_list
        self.body = body
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n

    def print(self):
        print_str = 'function name: %s, type: %s, params: %s, '
        print('function name: {}'.format(self.name))
        print('\ttype: {}'.format(self.type))
        print('\tparams: {}'.format(self.param_list))
        print('\tbody: {}'.format(self.body))


class Binop(Node):
    def __init__(self, left, binop, right):
        self.left = left
        self.binop = binop
        self.right = right
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n

    def evaluate(self):
        l = self.left.evaluate()
        # print(l)
        r = self.right.evaluate()
        # print(r)
        if l and r:
            # print(str(l), self.binop, str(r))
            return eval(str(l) + self.binop + str(r))
        else:
            return None


class DeclStmt(Node):
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.value = None
        self.lineno = None

    def setlineno(self, i):
        self.lineno = i


class For(Node):
    def __init__(self, init_stmt, cond_stmt, incr_stmt, body):
        self.init_stmt = init_stmt
        self.cond_stmt = cond_stmt
        self.incr_stmt = incr_stmt
        self.body = body
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class If(Node):
    def __init__(self, cond_stmt, body, else_body):
        self.cond_stmt = cond_stmt
        self.body = body
        self.else_body = else_body
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class Assignment(Node):
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


# TODO should make evaluation to handle formatting.
class Printf(Node):
    def __init__(self, arguments):
        self.arguments = arguments
        self.lineno = None

    def setlineno(self, n):
        self.lineno = n


class NodeList(Node):
    def __init__(self, node=None):
        self.nodes = []
        self.lineno = None
        self.type = None
        if node:
            self.nodes.append(node)


class StmtList(NodeList):
    # def __init__(self):
    #     self.stmtlist = []
    #     self.lineno = None

    def setlineno(self, n):
        self.lineno = n

    def add(self, stmt):
        self.nodes.append(stmt)


class DeclStmtList(NodeList):
    # def __init__(self, type):
    #     self.decllist = []
    #     self.type = type
    #     self.lineno = None

    def setlineno(self, n):
        self.lineno = n

    def add(self, stmt):
        self.nodes.append(stmt)

    def settype(self, type):
        self.type = type

    def gettype(self):
        return self.type


class ParameterList(NodeList):
    # def __init__(self):
    #     self.paramlist = []
    #     self.lineno = None

    def setlineno(self, n):
        self.lineno = n

    def add(self, arg):
        self.nodes.append(arg)


class ArgumentList(NodeList):
    # def __init__(self):
    #     self.arglist = []
    #     self.lineno = None

    def setlineno(self, n):
        self.lineno = n

    def add(self, arg):
        self.nodes.append(arg)


class GlobalList(NodeList):
    # def __init__(self):
    #     self.globallist = []
    #     self.symboltable = None
    #     self.lineno = None

    def setlineno(self, n):
        self.lineno = n

    def add(self, func):
        self.nodes.append(func)

    def print(self):
        print('In functionlist ,')
        print(self)
        for func in self.nodes:
            print(func)


# class ReturnStmt:
#     def __init__(self, expr):
#         self.expr = expr
