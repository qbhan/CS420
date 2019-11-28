class Null:
    def __init__(self):
        self.type = 'void'

    # def is_null(self):
    #     return True


class Type:
    def __init__(self, type):
        self.type = type


class PointerType:
    def __init__(self, pnttype):
        self.pnttype = pnttype


class FunctionType:
    def __init__(self, functype):
        self.functype = functype


class Constant:
    def __init__(self, value):
        self.type = type(value).__name__
        self.value = value
        # self.lineno = lineno

    # def is_const(self):
    #     return True

    def evaluate(self):
        return self.value


class Identifier:
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno

    def is_id(self):
        return True


class Pointer:
    def __init__(self, expr):
        self.expr = expr


class Binop:
    def __init__(self, left, binop, right):
        self.left = left
        self.binop = binop
        self.right = right

    def evaluate(self):
        l = self.left.evaluate()
        r = self.right.evaluate()
        if not l or not r:
            return eval(str(l) + self.binop + str(r))
        else:
            return None


class Negation:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        return -self.expr.evaluate()


class GetValue:
    def __init__(self, expr):
        self.expr = expr


    # need to make memory
    # def evaluate(self):
    #     return memory[self.expr.evaluate()]


class GetAddress:
    def __init__(self, expr):
        self.expr = expr

    # def evaluate(self):
    #     return memory.index(self.expr.evaluate)


class Increment:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        return self.expr.evaluate() + 1


class DeclStmt:
    def __init__(self, type, name):
        self.type = type
        self.name = name


class StmtList:
    def __init__(self, stmt):
        self.stmtlist = []

    def add(self, stmt):
        self.stmtlist.append(stmt)


class ParameterList:
    def __init__(self, param):
        self.paramlist = []
        if param:
            self.paramlist.append(param)

    def add(self, arg):
        self.arglist.append(arg)


class ArgumentList:
    def __init__(self, arg):
        self.arglist = []
        if arg:
            self.arglist.append(arg)

    def add(self, arg):
        self.arglist.append(arg)


class ReturnStmt:
    def __init__(self, expr):
        self.expr = expr


class ForStmt:
    def __init__(self, init_stmt, cond_stmt, incr_stmt, body):
        self.init_stmt = init_stmt
        self.cond_stmt = cond_stmt
        self.incr_stmt = incr_stmt
        self.body = body
        # self.lineno = lineno


class IfStmt:
    def __init__(self, cond_stmt, body, else_body):
        self.cond_stmt = cond_stmt
        self.body = body
        self.else_body = else_body
        # self.lineno = lineno


class StmtBlock:
    def __init__(self, stmt_list, sym_table):
        self.stmt_list = stmt_list
        self.sym_table = sym_table
        # self.lineno = lineno


class Function:
    def __init__(self, type, name, arg_list, body):
        self.type = type
        self.name = name
        self.arg_list = {i: None for i in arg_list}
        self.body = body
        # self.lineno = lineno


class FunctionCall:
    def __init__(self, function, arglist):
        self.function = function
        self.arglist = arglist


class Array:
    def __init__(self, name, type, length):
        self.type = type
        self.name = name
        self.length = length
        self.value = None
        # self.lineno = lineno

    def assign_value(self, value):
        if type(value) == list:
            self.value = value

    def is_int_pnt(self):
        return self.type == 'int'

    def is_float_pnt(self):
        return self.type == 'float'

    def index(self, i):
        if self.value:
            return self.value[i]

    def assign_index_value(self, value, i):
        if self.value:
            self.value[i] = value