import ply.yacc as yacc
from CS420.pyclexer import *


precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
    ('right', 'UMINUS')
)


def p_statement(p):
    '''stmt : expr SEMICOLON
            | local_declaration
            | stmt_block
            | SEMICOLON'''
    if p[1] != ';':
        p[0] = p[1]


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


def p_expr_assign( p ):
    '''expr : ID EQUAL expr'''
    p[0] = p[3]


def p_expr_basic( p ):
    '''expr : basic_expr'''
    p[0] = p[1]


def p_basic_expr_compare(p):
    '''basic_expr : basic_expr compare arith_expr'''
    if p[2] == '==':
        p[0] = p[1]==p[3]
    elif p[2] == '!=':
        p[0] = p[1]!=p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[3] == '<':
        p[0] = p[1] < p[3]


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
#
# def p_arith_parens(p):
#     '''arith_expr : LPAREN arith_expr RPAREN'''
#     p[0] = p[2]
#
# def p_arith_add(p):
#     '''arith_expr : arith_expr PLUS arith_expr'''
#     p[0] = p[1] + p[3]
#
# def p_arith_sub(p):
#     '''arith_expr : arith_expr MINUS arith_expr'''
#     p[0] = p[1] - p[3]
#
# def p_arith_mult(p):
#     '''arith_expr : arith_expr TIMES arith_expr'''
#     p[0] = p[1] * p[3]
#
# def p_arith_div(p):
#     '''arith_expr : arith_expr DIV arith_expr'''
#     if p[3] != 0:
#         p[0] = p[1] / p[3]
#     else:
#         raise ZeroDivisionError('Divison by 0')
#
# def p_arith_id(p):
#     '''arith_expr : ID'''
#     p[0] = p[1]

def p_arith_fnum(p):
    '''arith_expr : FNUM'''
    p[0] = float(p[1])

def p_arith_inum(p):
    '''arith_expr : INUM'''
    p[0] = int(p[1])

def p_empty(p):
    'empty :'
    pass

def p_error( p ):
    print("Syntax error in input!", p)

parser = yacc.yacc()

res = parser.parse("1") # the input
print(res)