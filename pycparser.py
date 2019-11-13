from ply import lex
import ply.yacc as yacc
from pyclexer import *

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
    ( 'nonassoc', 'UMINUS' )
)

# precedence = (
#     ( 'left', 'PLUS', 'MINUS' ),
#     ( 'left', 'TIMES', 'DIV' ),
# )

def p_expr_assign( p ):
    '''expr : ID EQUAL arith_expr'''
    p[0] = p[3]

def p_expr_bool( p ):
    '''expr : bool_expr'''
    p[0] = p[1]

def p_compare_expr_arith( p ):
    '''bool_expr : arith_expr'''
    p[0] = p[1]

def p_compare_expr_eq( p ):
    '''bool_expr : bool_expr EQ arith_expr'''
    p[0] = (p[1] == p[3])

def p_compare_expr_neq( p ):
    '''bool_expr : bool_expr NEQ arith_expr'''
    p[0] = (p[1] != p[3])

def p_compare_expr_gt( p ):
    '''bool_expr : bool_expr GT arith_expr'''
    p[0] = (p[1] > p[3])

def p_compare_expr_lt( p ):
    '''bool_expr : bool_expr LT arith_expr'''
    p[0] = (p[1] < p[3])



# def p_compare( p ):
#     '''compare : EQ
#             | NEQ
#             | GT
#             | LT'''

def p_add( p ) :
    'arith_expr : arith_expr PLUS arith_expr'
    p[0] = p[1] + p[3]

def p_sub( p ) :
    'arith_expr : arith_expr MINUS arith_expr'
    p[0] = p[1] - p[3]

def p_expr2uminus( p ) :
    'arith_expr : MINUS arith_expr %prec UMINUS'
    p[0] = - p[2]

def p_mult_div( p ) :
    '''arith_expr : arith_expr TIMES arith_expr
            | arith_expr DIV arith_expr'''

    if p[2] == '*' :
        p[0] = p[1] * p[3]
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]

def p_expr2NUM( p ) :
    'arith_expr : NUMBER'
    p[0] = p[1]

def p_parens( p ) :
    'arith_expr : LPAREN arith_expr RPAREN'
    p[0] = p[2]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

res = parser.parse("3 != 4*-1") # the input
print(res)

