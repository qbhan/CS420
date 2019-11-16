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

def p_expr_basic( p ):
    '''expr : basic_expr'''
    p[0] = p[1]

# def p_expr_inc1(p):
#     '''expr : inc1'''
#     p[0] = p[1] + 1
#
# def p_expr_inc2(p):
#     '''expr : inc2'''
#     p[0] = p[1]

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
        raise ZeroDivisionError('Divison by 0')
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

def p_factor_fnum(p):
    '''factor : FNUM'''
    p[0] = float(p[1])

def p_factor_inum(p):
    '''factor : INUM'''
    p[0] = int(p[1])

def p_empty(p):
    'empty :'
    pass

def p_error( p ):
    print("Syntax error in input!", p)

parser = yacc.yacc()

res = parser.parse("- 4 > - 3.45") # the input
print(res)
