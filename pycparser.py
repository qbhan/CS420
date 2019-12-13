import ply.yacc as yacc
from pyclexer import *
from datastructure import *
from pyclexer import *
from datastructure import *

##########################################################################
# Define precedence of operators.
# UMINUS (unary operator) is for negation of expression.
##########################################################################
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('right', 'UMINUS'),
)

error_flag = 0

##########################################################################
# Rules : Derive from Program
# A program contains variable declarations (which will be global).
# and function declaration.
# We represented a given program as a list of declarations.
##########################################################################
def p_program(p):
    '''program : declaration_list'''
    p[0] = p[1]


##########################################################################
# Rules : Derive list of (global) declarations
# Add both function and variable declaration to FunctionList(). -> AST
##########################################################################
# TODO Change name FunctionList() to something that makes more sense
def p_declaration_list_1(p):
    '''declaration_list : declaration_list func_declaration'''
    p[1].add(p[2])
    p[0] = p[1]


# TODO Add new declared variable to symbol table.
def p_declaration_list_2(p):
    '''declaration_list : declaration_list declaration SEMICOLON'''
    p[1].add(p[2])
    p[0] = p[1]


def p_declaration_list_3(p):
    '''declaration_list : empty'''
    p[0] = GlobalList()


##########################################################################
# Rules : Derive function declaration
# Make Function() object defined by given syntax. -> AST
##########################################################################
# TODO should implement symbol table to update scope of body of function
#  with parameters
def p_func_declaration_1(p):
    '''func_declaration : type ID LPAREN params RPAREN stmt_block'''

    p[0] = Function(p[1], p[2], p[4], p[6])


def p_func_declaration_2(p):
    '''func_declaration : type TIMES ID LPAREN params RPAREN stmt_block'''

    p[0] = Function(Pointer(p[1]), p[2], p[4], p[6])


def p_func_declaration_3(p):
    '''func_declaration : type MAIN LPAREN params RPAREN stmt_block'''

    p[0] = Function(p[1], 'main', p[4], p[6])


##########################################################################
# Rules : Derive list of parameters.
# Make ParameterList() object and add each parameter declarations -> AST.
# Handle 2 cases : no parameter / parameter with types.
##########################################################################
def p_params_1(p):
    '''params : VOID'''
    p[0] = ParameterList()


def p_params_2(p):
    '''params : param_list'''
    p[0] = p[1]


def p_param_list_1(p):
    '''param_list : param'''

    p[0] = ParameterList()
    p[0].add(p[1])


def p_param_list_2(p):
    '''param_list : param_list COMMA param'''

    p[1].add(p[3])
    p[0] = p[1]


##########################################################################
# Rules : Derive each parameter declaration.
# Make DeclStmt() object for each parameter declaration -> AST.
# Handle 2 cases : Basic type parameter / Pointer type parameter
##########################################################################
# TODO try to merge with declaration below for simple grammar
def p_param_1(p):
    '''param : type ID'''

    p[0] = DeclStmt(p[1], Identifier(p[2], p.lineno(2)))


def p_param_2(p):
    '''param : type TIMES ID'''

    p[0] = DeclStmt(Pointer(p[1]), Identifier(p[3], p.lineno(3)))


##########################################################################
# Rules : Derive general statement & Handle dangling-ELSE problem.
# Make IF() object if IF statement is found -> AST.
# Refered what we have learned in class solving ambiguity.
##########################################################################
def p_general_statement(p):
    '''genstmt : mstmt
                | umstmt'''
    p[0] = p[1]


def p_matched_statement(p):
    '''mstmt : IF LPAREN expr RPAREN mstmt ELSE mstmt
                | stmt'''
    if p[1] == "if":
        p[0] = If(p[3], p[5], p[7])
        p[0].setlineno(p.lineno(1))
    else: p[0] = p[1]


def p_unmatched_statement(p):
    '''umstmt : IF LPAREN expr RPAREN genstmt
                | IF LPAREN expr RPAREN mstmt ELSE umstmt'''
    if len(p) == 6:
        p[0] = If(p[3], p[5], None)
    elif len(p) == 8:
        p[0] = If(p[3], p[5], p[7])
    p[0].setlineno(p.lineno(1))



##########################################################################
# Rules : Derive basic statement.
# Derive 7 kinds of statements : basic expression / local declaration /
# one block of statement / FOR statement / RETURN statement /
# empty statement / printf() function calling statement.
##########################################################################
# TODO might merge emty statement with expr statement by making expr empty
def p_statement(p):
    '''stmt : expr SEMICOLON
            | declaration SEMICOLON
            | stmt_block
            | stmt_forloop
            | stmt_return
            | SEMICOLON'''

    if p[1] != ';':
        if len(p) > 2 and p[2] == ';':
            p[1].setlineno(p.lineno(2))
        p[0] = p[1]
    else:
        p[0] = None


def p_statement_error_1(p):
    '''stmt : expr error'''
    print('statement lack semicolon line :', int(p.lineno(2)) - 1)


# def p_statement_error_2(p):
#     '''stmt : error stmt_forloop'''
#     print('statement lack semicolon line :', p.lineno(1))


##########################################################################
# Rules : Derive calling prinf() function
##########################################################################
def p_stmt_printf(p):
    '''stmt : PRINT LPAREN argument_list RPAREN'''
    p[0] = Printf(p[3])


##########################################################################
# Rules : Derive local declarations
# Handles multi local declarations in one statement with 2 types :
# Basic type / Pointer Type
# DeclStmt will get declaration with list object.
##########################################################################
# def p_declaration_1(p):
#     '''declaration : declaration COMMA idbracket'''
#     ty = p[1].gettype()
#     p[1].add(DeclStmt(ty, p[2]))
#     p[0] = p[1]
#
# def p_declaration_2(p):
#     '''declaration : declaration COMMA TIMES idbracket'''
#     ty = p[1].gettype()
#     p[1].add(DeclStmt(PointerType(ty), p[3]))
#     p[0] = p[1]
#
#
# def p_declaration_3(p):
#     '''declaration : type idbracket'''
#     p[0] = DeclStmtList(DeclStmt(p[1], p[2]))
#     p[0].settype(p[1])
#
#
# def p_declaration_4(p):
#     '''declaration : type TIMES idbracket'''
#     p[0] = DeclStmtList(DeclStmt(PointerType(p[1]), p[3]))
#     p[0].settype(PointerType(p[1]))

def p_declaration_1(p):
    '''declaration : declaration COMMA idbracket'''
    ty = p[1].gettype()
    if type(p[3]).__name__ == 'Array':
        length = p[3].length
        name = p[3].name
        p[1].add(DeclStmt(ArrayType(ty, length), Identifier(name, None)))
    else:
        p[1].add(DeclStmt(ty, p[3]))
    p[0] = p[1]

def p_declaration_2(p):
    '''declaration : declaration COMMA TIMES idbracket'''
    ty = p[1].gettype()
    if type(p[4]).__name__ == 'Array':
        length = p[4].length
        name = p[4].name
        p[1].add(DeclStmt(ArrayType(PointerType(ty), length), Identifier(name, None)))
    else:
        p[1].add(DeclStmt(PointerType(ty), p[4]))
    p[0] = p[1]


def p_declaration_3(p):
    '''declaration : type idbracket'''
    p[0] = DeclStmtList(p[1])
    if type(p[2]).__name__ == 'Array':
        length = p[2].length
        name = p[2].name
        p[0].add(DeclStmt(ArrayType(p[1], length), Identifier(name, None)))
    else:
        p[0].add(DeclStmt(p[1], p[2]))


def p_declaration_4(p):
    '''declaration : type TIMES idbracket'''
    p[0] = DeclStmtList(p[1])
    if type(p[3]).__name__ == 'Array':
        length = p[3].length
        name = p[3].name
        p[0].add(DeclStmt(ArrayType(PointerType(p[1]),length), Identifier(name, None)))
    else:
        p[0].add(DeclStmt(PointerType(p[1]), p[3]))

##########################################################################
# Rules : Derive id_list & id_bracket
# Handles whether declared identifier contais constant or array.
# Then add declared identifier to id_list.
##########################################################################
# TODO might use id_bracket to arith_expr when calling identifier for
#  simple grammar
def p_id_bracket_1(p):
    '''idbracket : ID'''
    p[0] = Identifier(p[1], p.lineno(1))


def p_id_bracket_2(p):
    '''idbracket : ID LBRACKET INUM RBRACKET'''
    p[0] = Array(p[1], p[3])
##########################################################################
# Rules : Derive basic types
##########################################################################
def p_type(p):
    '''type : INT
            | FLOAT
            | VOID'''

    p[0] = p[1]


##########################################################################
# Rules : Derive statement block.
# Statement block refers to statements inside closed brackets.
# Contains list of statements represented as non-terminal 'stmt_list'
##########################################################################
def p_stmt_block(p):
    '''stmt_block : LBRACE stmt_list RBRACE'''
    # Need to implement scope inside

    p[0] = p[2]
    p[0].setlineno(p.lineno(1))


##########################################################################
# Rules : Derive statement list
# Generate StmtList() object and add each statement object in order.
##########################################################################
def p_stmt_list_1(p):
    '''stmt_list : stmt_list genstmt'''

    p[1].add(p[2])
    p[0] = p[1]


def p_stmt_list_2(p):
    '''stmt_list : empty'''

    p[0] = StmtList()

##########################################################################
# Rules : Derive FOR statement
# Generate For() object
##########################################################################
def p_forloop(p):
    '''stmt_forloop : FOR LPAREN expr SEMICOLON expr SEMICOLON expr RPAREN stmt'''
    p[0] = For(p[3], p[5], p[7], p[9])
    p[0].setlineno(p.lineno(1))

# def p_forloop_error_1(p):
#     '''stmt_forloop : error FOR LPAREN expr SEMICOLON expr SEMICOLON expr RPAREN stmt'''
#     print('error in line no :', p.lineno(1))


##########################################################################
# Rules : Derive RETURN statement
# Generate ReturnStmt() object in 2 types : return something / nothing.
##########################################################################
def p_return_stmt_1(p):
    '''stmt_return : RETURN expr SEMICOLON'''

    p[0] = ReturnStmt(p[2])
    p[0].setlineno(p.lineno(3))


def p_return_stmt_2(p):
    '''stmt_return : RETURN SEMICOLON'''

    p[0] = ReturnStmt(None)
    p[0].setlineno(p.lineno(2))


##########################################################################
# Rules : Derive expressions.
# Expression with 3 kinds of assignment : identifier / array indexing /
# pointer
# Expression with incrementing expression
##########################################################################
# TODO should implement symbol table to update changed value and history.
# TODO might use id_bracket above to simplify grammar
def p_expr_assign_1(p):
    '''expr : ID EQUAL expr'''
    id = Identifier(p[1], p.lineno(1))
    p[0] = Assignment(id, p[3])

    # get class identifier from symbol table and assign


def p_expr_assign_2(p):
    '''expr : ID LBRACKET arith_expr RBRACKET EQUAL expr'''
    p[0] = Assignment(Array_index(p[1], p[3]), p[6])


def p_expr_assign_3(p):
    '''expr : TIMES ID EQUAL expr'''
    p[0] = Assignment(Pointer(p[2]), p[4])


def p_expr_incr(p):
    '''expr : incr_expr'''
    p[0] = p[1]

##########################################################################
# Rules : Derive basic expression (Boolean, comparing)
##########################################################################
def p_expr_basic(p):
    '''expr : basic_expr'''
    # print('basic_expr')
    p[0] = p[1]


def p_basic_expr_compare(p):
    '''basic_expr : basic_expr compare arith_expr'''
    # if p[2] == '==':
    #     p[0] = p[1] == p[3]
    # elif p[2] == '!=':
    #     p[0] = p[1] != p[3]
    # elif p[2] == '>':
    #     p[0] = p[1] > p[3]
    # elif p[3] == '<':
    #     p[0] = p[1] < p[3]

    p[0] = Binop(p[1], p[2], p[3])



def p_basic_expr_arith_expr(p):
    '''basic_expr : arith_expr'''
    # print('arith_expr')
    p[0] = p[1]


def p_compare(p):
    '''compare : EQ
               | NEQ
               | GT
               | LT'''

    p[0] = p[1]

##########################################################################
# Rules : Derive incrementing expression
##########################################################################
# TODO should we think about difference of ++a and a++?
def p_incr_expr_1(p):
    '''incr_expr : ID INCREMENT'''
    # ty = int
    # id = Identifier(p[2], ty.__name__)
    # id.incr()

    p[0] = Increment(p[1], True)


def p_incr_expr_2(p):
    '''incr_expr : INCREMENT ID'''
    # should check ID in symbol table
    # ty = int
    # id = Identifier(p[2], ty.__name__)
    # id.incr()

    p[0] = Increment(p[2], False)

##########################################################################
# Rules : Derive basic arithmetic expressions.
# Not much to say.
##########################################################################
def p_arith_uminus(p):
    '''arith_expr : MINUS arith_expr %prec UMINUS'''
    # p[0] = -p[2]

    p[0] = Negation(p[2])


def p_arith_parens(p):
    '''arith_expr : LPAREN arith_expr RPAREN'''
    # print('LPAREN arith_expr RPAREN')
    # global error_flag
    # error_flag = 1
    p[0] = p[2]

# def p_arith_parens_error(p):
#     '''arith_expr : LPAREN error'''
#     print('Syntax error in parentheses')


def p_arith_add(p):
    '''arith_expr : arith_expr PLUS arith_expr'''
    # print(p.lineno(2))
    # p[0] = p[1] + p[3]
    # print(p[0])
    # p[0] = bin_op(p[1], p[2], p[3])

    p[0] = Binop(p[1], p[2], p[3])


def p_arith_sub(p):
    '''arith_expr : arith_expr MINUS arith_expr'''
    # p[0] = p[1] - p[3]
    # print(p[0])
    # p[0] = bin_op(p[1], p[2], p[3])

    p[0] = Binop(p[1], p[2], p[3])


def p_arith_mult(p):
    '''arith_expr : arith_expr TIMES arith_expr'''
    # p[0] = p[1] * p[3]
    # print(p[0])
    # p[0] = bin_op(p[1], p[2], p[3])

    p[0] = Binop(p[1], p[2], p[3])


def p_arith_div(p):
    '''arith_expr : arith_expr DIV arith_expr'''
    # if p[3] != 0:
    #     p[0] = p[1] / p[3]
    #     print(p[0])
    # else:
    #     raise ZeroDivisionError('Divison by 0')
    # print(p[0])

    p[0] = Binop(p[1], p[2], p[3])


# TODO might find way to simplify grammar when assigning value to arith_expr
#  using id_bracket above or other
def p_arith_id(p):
    '''arith_expr : ID'''
    # p[0] = p[1]
    # access symbol table and get id as identifier class
    # ty = int

    p[0] = Identifier(p[1], p.lineno(1))


def p_arith_fnum(p):
    '''arith_expr : FNUM'''
    # p[0] = float(p[1])
    # p[0] = constant(float(p[1]))

    p[0] = Constant(float(p[1]))


def p_arith_inum(p):
    '''arith_expr : INUM'''
    # print(p.lineno(1))
    # p[0] = int(p[1])

    p[0] = Constant(int(p[1]))


# TODO should implement symbol table to refer to
def p_arith_pointer(p):
    '''arith_expr : TIMES ID'''
    p[0] = Pointer(p[2])

# TODO should implement symbol table to refer to
def p_arith_address(p):
    '''arith_expr : ADDRESS ID'''
    p[0] = Address(p[2])

# TODO should implement symbol table to refer to
def p_arith_array_index(p):
    '''arith_expr : ID LBRACKET arith_expr RBRACKET'''
    # for arith_expr, should evaluate&assign, or just assign?
    p[0] = Array_index(p[1], p[3])


def p_arith_pointer_array(p):
    '''arith_expr : TIMES ID LBRACKET arith_expr RBRACKET'''
    p[0] = Pointer(Array_index(p[2], p[3]))


def p_arith_functioncall(p):
    '''arith_expr : ID LPAREN argument_list RPAREN'''
    p[0] = FunctionCall(p[1], p[3])

# def p_arith_functioncall_error_1(p):
#     '''arith_expr : ID LPAREN argument_list RPAREN'''
#     print('Unclosed functioncall ignored in line :', p.lineno(4))
#     # p[0] = p[4]


# def p_arith_error(p):
#     '''arith_expr : error'''
#     print('arith_expr error in line :', p.lineno(1))


##########################################################################
# Rules : Derive arguments for function call.
##########################################################################
def p_argument_list_1(p):
    '''argument_list : argument'''
    p[0] = ArgumentList()
    if p[1]:
        p[0].add(p[1])


def p_argument_list_2(p):
    '''argument_list : argument_list COMMA argument'''
    p[1].add(p[3])
    p[0] = p[1]


def p_argument_1(p):
    '''argument : empty'''
    p[0] = None


def p_argument_2(p):
    '''argument : arith_expr'''
    # for arith_expr, should evaluate&assign, or just assign?
    p[0] = p[1]


def p_argument_3(p):
    '''argument : LITERAL'''

    p[0] = Literal(p[1])


def p_argument_error(p):
    '''argument : error'''
    print('wrong argument ignored in line :', p.lineno(1))
    p[0] = p[1]


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    # print('Syntax error not handled!!!')
    print("Syntax error in input!", p)



# parser = yacc.yacc()

# res = parser.parse("int main (){x = 1;\n1+1*2;\n}")  # the input

# input = ''
# f = open('test.txt', 'r')
# while True:
#     line = f.readline()
#     input += line
#     if not line:
#         break
#     # lexer.input(line)
#     # while True:
#     #     tok = lexer.token()
#     #     if not tok:
#     #         break
#     #     print(tok)
# f.close()
# # print(input)

# res = parser.parse(input)

# print(res)
# print(res.funclist[0].print())
# print(res.nodes[1].body.nodes[1].nodes)