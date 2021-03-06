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


class Node:
    def __init__(self, value, parent, left, right):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class Function:
    def __init__(self, type, name, arg_list, body):
        self.type = type
        self.name = name
        self.arg_list = {i: None for i in arg_list}
        self.body = body


class Array:
    def __init__(self, name, type, length):
        self.type = type
        self.name = name
        self.length = length
        self.value = None

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


class Identifier:
    def __init__(self, name, type):
        self.type = type
        self.name = name
        self.value = None

    def assign_value(self, value):
        self.value = value

    def is_int(self):
        return self.type == 'int'

    def is_float(self):
        return self.type == 'float'

    def is_pointer(self):
        return self.type == 'intpointer' or self.type == 'floatpointer'

    def assign(self, a):
        if self.is_int():
            self.assign_value(int(a.value))
        elif self.is_float():
            self.assign_value(float(a.value))

    def neg(self):
        self.value = -self.value

    def print(self):
        print('id name : ' + self.name + ', type : ' + self.type + ', value : ' + str(self.value))


class Constant:
    def __init__(self, value):
        self.type = type(value).__name__
        self.value = value

    def is_int(self):
        return self.type == 'int'

    def is_float(self):
        return self.type == 'float'

    def neg(self):
        self.value = -self.value

    def print(self):
        print('const type : ' + str(self.type) + ', value : ' + str(self.value))


class Stmt_block:
    def __init__(self, stmt_list, sym_table):
        self.stmt_list = stmt_list
        self.sym_table = sym_table


class Stmt:
    def __init__(self, ast, lineno):
        self.ast = ast
        self.lineno = lineno


def bin_op(a, op, b):
    if op == '+':
        add(a, b)
    elif op == '-':
        sub(a, b)
    elif op == '*':
        mult(a, b)
    elif op == '/':
        div(a, b)
    elif op == '==':
        return a.value == b.value
    elif op == '!=':
        return a.value != b.value
    elif op == '>':
        return a.value > b.value
    elif op == '<':
        return a.value < b.value


def add(a, b):
    new_value = a.value + b.value
    return Constant(new_value)


def sub(a, b):
    new_value = a.value - b.value
    return Constant(new_value)


def mult(a, b):
    new_value = a.value * b.value
    return Constant(new_value)


def div(a, b):
    new_value = a.value / b.value
    if a.is_int() and b.is_int():
        new_value = int(new_value)
    return Constant(new_value)








# print(float(1))
a = Constant(4)
# print(type(a))
# c = constant(3)
# div(a,c).print()
