from ply import lex
import ply.yacc as yacc
from pyclexer import *

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
)



# statement derived to expression, declaration, statement block and ;
def p_statement(p):
    '''stmt : expr
            | declaration
            | stmt_block
            | SEMICOLON'''
    if p[1] != ';':
        p[0] = p[1]

# declaration with type of int, float, and void (not implemented pointer yet)
def p_declaration(p):
    '''declaration : INT ID SEMICOLON
                   | FLOAT ID SEMICOLON
                   | VOID ID SEMICOLON'''
    # Need to implement adding to symbol table


def p_stmt_block(p):
    '''stmt_block : LBRACE stmt_list RBRACE'''
    # Need to implement scope inside

def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | empty'''

# expression divided to assignment and boolean value itself
def p_expr_assign( p ):
    '''expr : ID EQUAL expr'''
    p[0] = p[3]

def p_expr_bool( p ):
    '''expr : bool_expr'''
    p[0] = p[1]

# boolean expression might be a number(0 or not), or a comparison
# comparison with EQ, NEQ, GT, LT
def p_bool_expr_arith( p ):
    '''bool_expr : arith_expr'''
    p[0] = p[1]

def p_bool_expr_eq( p ):
    '''bool_expr : bool_expr EQ arith_expr'''
    p[0] = (p[1] == p[3])

def p_bool_expr_neq( p ):
    '''bool_expr : bool_expr NEQ arith_expr'''
    p[0] = (p[1] != p[3])

def p_bool_expr_gt( p ):
    '''bool_expr : bool_expr GT arith_expr'''
    p[0] = (p[1] > p[3])

def p_bool_expr_lt( p ):
    '''bool_expr : bool_expr LT arith_expr'''
    p[0] = (p[1] < p[3])


# Basic arithmetic expression and calculation
# increment not done yet
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

def p_empty(p):
    'empty :'
    pass

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

res = parser.parse("3 + -4") # the input
print(res)

