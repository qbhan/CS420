from ply import lex
import ply.yacc as yacc
from pyclexer import *

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
)

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

def p_arith_add(p):
    '''arith_expr : arith_expr PLUS term'''
    p[0] = p[1] + p[3]

def p_arith_sub(p):
    '''arith_expr : arith_expr MINUS term'''
    p[0] = p[1] - p[3]

def p_arith_term(p):
    '''arith_expr : term'''
    p[0] = p[1]

def p_term_mult(p):
    '''term : term TIMES factor'''
    p[0] = p[1] * p[3]

def p_term_div(p):
    '''term : term DIV factor'''
    if p[3] == 0:
        raise ZeroDivisionError('integer division by 0')
    p[0] = p[1] / p[3]

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_parens(p):
    '''factor : LPAREN expr RPAREN'''
    p[0] = p[2]

def p_factor_neg(p):
    '''factor : MINUS factor'''
    p[0] = -p[2]

def p_factor_id(p):
    '''factor : ID'''
    p[0] = p[1]

def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = p[1]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

res = parser.parse("3 + 4") # the input
print(res)

