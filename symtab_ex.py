import sys

# We make symbol table entry here, and make symbol table as a node.
symbol_Table_Entry = {}
#tracks number of keys
attribute_Value = 0

# import hashlib

# When lexing int a;
# Tokens will be made as follows
token_variable_ex = [['INT', 'int', 0, 0], ['ID', 'a', 0, 4], ['SEMICOLON',';', 0, 5]]
token_function_ex = [['INT', 'int', 1, 0], ['ID', 'a', 1, 4], ['LPAREN', '(', 1, 5], ['INT', 'int', 1, 6], ['ID', 'x', 1, 10], ['COMMA', ',', 1, 11], ['FLOAT', 'float', 1, 13], ['ID', 'y', 1, 18], ['RPAREN', ')', 1, 19], ['LBRACE', '{', 1, 20]]
token_array_ex = [['INT', 'int', 2, 0], ['ID', 'a', 2, 4], ['LBRACKET', '[', 2, 5], ['NUMBER', 3, 2, 6], ['RBRACKET', ']', 2, 7], ['SEMICOLON',';', 0, 8]]
token_pointer_ex = [['INT', 'int', 3, 0],['POINTER', '*', 3, 4],['ID', 'a', 3, 5],['SEMICOLON', ';', 3, 5]]




class Var(object):
    token_type = 'variable'

    def __init__(self, var=None):
        self.line_No = var[0][2]

        # token_Name: string
        self.token_Name = var[1][1]
        # var_Type: string
        self.var_Type = var[0][1]

        # Command 'trace' in Terminal prints out N/A in the line the variable is defined.
        self.int_Value = sys.maxsize
        self.float_Value = sys.float_info.max

    def assign_value(self, value):
        self.int_Value = int(value)
        self.float_Value = float(value)


class Func(object):
    token_type = 'function'

    def __init__(self, fun=None):

        # Count how many parameters function has.
        # Warning! parameter could be either variable or parameter!
        # self.param_Num = 0
        # param_Token = fun[]
        # while not
        pass


class Array(object):
    token_type = 'array'

    def __init__(self, arr=None):
        self.line_No = arr[0][2]

        self.token_Name = arr[1][1]
        self.var_Type = arr[0][1]

        # Array size due to make each elements an object
        self.array_Size = arr[3][1]
        # Do we have to code an array of pointers? e.g. int* a[10];
        for i in range(0, self.array_Size + 1):

            # Defining each elements as an object
            # e.g. We use a[1] as a variable with name of 'a[1]'
            tokens = [['',self.var_Type, self.line_No,0], ['', self.token_Name + "[" + str(i) + "]", 0, 0], ['','',0,0]]
            variable = Var(tokens)

            # use global var attributed_Value: to put each elements in the symbol table.
            global attribute_Value
            symbol_Table_Entry[attribute_Value] = variable
            attribute_Value += 1


class Pointer(object):
    token_type = 'pointer'

    def __init__(self, ptr=None):

        pass



class SymbolEntry:

    def __init__(self, name, value, scope):
        self.name = name
        self.value = value
        self.inner = None # Must be of class type SymbolTable
        self.scope = scope

    def setNestedScope(SymbolTable):

        self.inner = SymbolTable
        self.inner.parent = self.scope

class SymbolTable:
    
    def __init__(self, scope):
        self.content = {}
        self.parent = None # Must be ID of the parent symbol table
        self.scope = scope


    def pushSymbol(self, SymbolEntry):
        name = SymbolEntry.name
        self.content[name] = SymbolEntry
        self.content[name].scope = self.scope


# Symbol Table methods:
# Update, load History, load current Value
# value is an Object --> has [(value, line no.), ...] which is history, -1 index is the most current





#routine for filling in the symbol table may need to be re-considered





var_1 = Var(token_variable_ex)
symbol_Table_Entry[attribute_Value] = var_1
attribute_Value += 1
arr_1 = Array(token_array_ex)
symbol_Table_Entry[attribute_Value] = arr_1
attribute_Value += 1
print(symbol_Table_Entry[0].token_Name, symbol_Table_Entry[1].token_Name, symbol_Table_Entry[5].token_Name, attribute_Value)