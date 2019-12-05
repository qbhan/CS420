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
        return self._accept(self.__class__, visitor)

    def _accept(self, klass, visitor):
        visitor_method = getattr(visitor, klass.__name__, None)
        if visitor_method == None:
            base = klass.__bases__
            return self._accept(base, visitor)
        else:
            return visitor_method(self)


class Unary(Node):

    def __init__(self, node):
        self.expr = node


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
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        return self.expr.evaluate() + 1


class ReturnStmt(Node):

    def __init__(self, expr):
        self.expr = expr


class StmtBlock(Node):
    def __init__(self, stmt_list, sym_table):
        self.stmt_list = stmt_list
        self.sym_table = sym_table
        # self.lineno = lineno


class FunctionCall(Node):
    def __init__(self, function, arglist):
        self.function = function
        self.arglist = arglist


class Constant:
    def __init__(self, value):
        self.type = type(value).__name__
        self.value = value
        # self.lineno = lineno

    # def is_const(self):
    #     return True

    def evaluate(self):
        return self.value

##########################################################################
# Made for string literals for printf usage.
##########################################################################
class Literal:
    def __init__(self, literal):
        self.value = literal


class Identifier:
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

    def is_id(self):
        return True


class Pointer:
    def __init__(self, id):
        self.id = id


##########################################################################
# Address : For cases like &a
##########################################################################
class Address:
    def __init__(self, value):
        self.value = value


class Array:
    def __init__(self, name, type, length):
        self.type = type
        self.name = name
        self.length = length


class Array_index:
    def __init__(self, name, index):
        self.name = name
        self.index = index


class Function:
    def __init__(self, type, name, param_list, body):
        self.type = type
        self.name = name
        self.param_list = param_list
        self.body = body
        # self.lineno = lineno

    def print(self):
        print_str = 'function name: %s, type: %s, params: %s, '
        print('function name: {}'.format(self.name))
        print('\ttype: {}'.format(self.type))
        print('\tparams: {}'.format(self.param_list))
        print('\tbody: {}'.format(self.body))


class Binop:
    def __init__(self, left, binop, right):
        self.left = left
        self.binop = binop
        self.right = right

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


# class Negation:
#     def __init__(self, expr):
#         self.expr = expr
#
#     def evaluate(self):
#         return -self.expr.evaluate()




# class GetValue:
#     def __init__(self, expr):
#         self.expr = expr

    # need to make memory
    # def evaluate(self):
    #     return memory[self.expr.evaluate()]





# class GetAddress:
#     def __init__(self, expr):
#         self.expr = expr

    # def evaluate(self):
    #     return memory.index(self.expr.evaluate)





# class Increment:
#     def __init__(self, expr):
#         self.expr = expr
#
#     def evaluate(self):
#         return self.expr.evaluate() + 1


class DeclStmt:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.value = None


class For:
    def __init__(self, init_stmt, cond_stmt, incr_stmt, body):
        self.init_stmt = init_stmt
        self.cond_stmt = cond_stmt
        self.incr_stmt = incr_stmt
        self.body = body


class If:
    def __init__(self, cond_stmt, body, else_body):
        self.cond_stmt = cond_stmt
        self.body = body
        self.else_body = else_body


class Assignment:
    def __init__(self, id, value):
        self.id = id
        self.value = value


# TODO should make evaluation to handle formatting.
class Printf:
    def __init__(self, arguments):
        self.arguments = arguments


class StmtList:
    def __init__(self):
        self.stmtlist = []

    def add(self, stmt):
        self.stmtlist.append(stmt)


class ParameterList:
    def __init__(self):
        self.paramlist = []

    def add(self, arg):
        self.paramlist.append(arg)


class ArgumentList:
    def __init__(self):
        self.arglist = []

    def add(self, arg):
        self.arglist.append(arg)


class GlobalList:
    def __init__(self):
        self.globallist = []
        self.symboltable = None

    def add(self, func):
        self.globallist.append(func)

    def print(self):
        print('In functionlist ,')
        print(self)
        for func in self.globallist:
            print(func)


# class ReturnStmt:
#     def __init__(self, expr):
#         self.expr = expr
