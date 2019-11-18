import ply.yacc as yacc
from CS420.pyclexer import *
from CS420.datastructure import *


from CS420.datastructure import constant, div

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('right', 'UMINUS'),

)


def p_program(p):
    '''program : func_declaration_list'''
    # need to implement


#
def p_func_declaration_list_1(p):
    '''func_declaration_list : func_declaration_list func_declaration'''


def p_func_declaration_list_2(p):
    '''func_declaration_list : empty'''


#
def p_func_declaration(p):
    '''func_declaration : type ID LPAREN arg_list RPAREN stmt_block'''


#
#
def p_arg_list_1(p):
    '''arg_list : empty'''


def p_arg_list_2(p):
    '''arg_list : arg_list COMMA arg'''


#
def p_arg(p):
    '''arg : type ID'''
    p[0] =


# statement derived to expression, declaration,  and ;
def p_statement(p):
    '''stmt : expr SEMICOLON
            | local_declaration
            | stmt_block
            | stmt_return
            | SEMICOLON'''
    if p[1] != ';':
        p[0] = p[1]


# declaration with type of int, float, and void (not implemented pointer yet)
def p_local_declaration(p):
    '''local_declaration : type ID SEMICOLON
                   | type TIMES ID SEMICOLON
                   | type TIMES LBRACKET RBRACKET SEMICOLON'''
    # Need to implement adding to symbol table


def p_type(p):
    '''type : INT
            | FLOAT
            | VOID'''


def p_stmt_block(p):
    '''stmt_block : LBRACE stmt_list RBRACE'''
    # Need to implement scope inside


# #
def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | empty'''


# expression divided to assignment and boolean value itself
def p_expr_assign(p):
    '''expr : ID EQUAL expr'''
    p[0] = p[3]
    # get class identifier from symbol table and assign


def p_expr_basic(p):
    '''expr : basic_expr'''
    p[0] = p[1]


def p_return_stmt_1(p):
    '''stmt_return : RETURN expr SEMICOLON'''


def p_return_stmt_2(p):
    '''stmt_return : RETURN SEMICOLON'''


def p_basic_expr_compare(p):
    '''basic_expr : basic_expr compare arith_expr'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[3] == '<':
        p[0] = p[1] < p[3]
    # p[0] = bin_op(p[1], p[2], p[3])


def p_basic_expr_arith_expr(p):
    '''basic_expr : arith_expr'''
    p[0] = p[1]


def p_compare(p):
    '''compare : EQ
               | NEQ
               | GT
               | LT'''
    p[0] = p[1]


def p_arith_uminus(p):
    '''arith_expr : MINUS arith_expr %prec UMINUS'''
    p[0] = -p[2]
    # p[0] = p[2].neg()


def p_arith_parens(p):
    '''arith_expr : LPAREN arith_expr RPAREN'''
    p[0] = p[2]


def p_arith_add(p):
    '''arith_expr : arith_expr PLUS arith_expr'''
    p[0] = p[1] + p[3]
    print(p[0])
    # p[0] = bin_op(p[1], p[2], p[3])


def p_arith_sub(p):
    '''arith_expr : arith_expr MINUS arith_expr'''
    p[0] = p[1] - p[3]
    print(p[0])
    # p[0] = bin_op(p[1], p[2], p[3])


def p_arith_mult(p):
    '''arith_expr : arith_expr TIMES arith_expr'''
    p[0] = p[1] * p[3]
    print(p[0])
    # p[0] = bin_op(p[1], p[2], p[3])


def p_arith_div(p):
    '''arith_expr : arith_expr DIV arith_expr'''
    if p[3] != 0:
        p[0] = p[1] / p[3]
        print(p[0])
    else:
        raise ZeroDivisionError('Divison by 0')
    print(p[0])
    # p[0] = bin_op(p[1], p[2], p[3])


def p_arith_id(p):
    '''arith_expr : ID'''
    p[0] = p[1]
    # access symbol table and get id as identifier class
    # ty = int
    # p[0] = identifier(p[1], str(ty))


def p_arith_fnum(p):
    '''arith_expr : FNUM'''
    p[0] = float(p[1])
    # p[0] = constant(float(p[1]))


def p_arith_inum(p):
    '''arith_expr : INUM'''
    p[0] = int(p[1])
    # p[0] = constant(int(p[1]))


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print("Syntax error in input!", p)


parser = yacc.yacc()

res = parser.parse("int x (){int *x; x = 1; 1+1*4; 2*4+1; return ;}")  # the input
print(res)
# a = constant(4)
# c = constant(3)
# div(a,c).print()
