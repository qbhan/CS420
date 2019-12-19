import ply.lex as lex

# List of token names. This is always required
tokens = [

    'INUM',
    'FNUM',
    'ID',
    'LITERAL',

    # operators
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'INCREMENT',
    'ADDRESS',

    # comparison
    'EQ',
    'NEQ',
    'GT',
    'LT',

    # assignment
    'EQUAL',

    # closures
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'PERIOD',
    'SEMICOLON',
    'COLON',
    'QUOTE',
    'DOUBLEQUOTE',

    # statement forms
    'IF',
    'ELSE',
    'ELSE_IF',
    'FOR',

    # types
    'INT',
    'POINTER',
    'FLOAT',
    'VOID',

    # essentials
    'MAIN',
    'PRINT',
    'RETURN',
]

keyword = {'int': 'INT', 'float': 'FLOAT', 'if': 'IF', 'else': 'ELSE', 'else if': 'ELSE_IF', 'for': 'FOR', 'main': "MAIN", 'printf': 'PRINT', 'include': 'INCLUDE', 'return': 'RETURN', 'void': 'VOID'}

# Regular expression rules
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
r_NUM = r'[-]?[0-9]*\.?[0-9]+'
t_LITERAL = r'"([^"\n]|(\\"))*"'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_INCREMENT = r'\+\+'
t_ADDRESS = r'\&'

t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'
#
t_EQUAL = r'='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_PERIOD = r'\.'
t_SEMICOLON = r'\;'
t_COLON = r':'
t_QUOTE = r'\''
t_DOUBLEQUOTE = r'"'

# Define rule to get number

def t_FNUM(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_reserved(t):
    r'[a-zA-Z_$][a-zA-Z0-9_$]*'
    if t.value in keyword:
        t.type = keyword[t.value]
    else:
        t.type = 'ID'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# read file in same directory by line
# comment it when not in use
# f = open('test.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     lexer.input(line)
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         print(tok)
# f.close()


# Give the lexer some input
# lexer.input('++\"abc\"')
# lexer.input(r'"string"')
# lexer.input("int x (){\nint *x;\n x = 1;\n 1+1*4;\n 2*4+1;\n return ;\n}")

# Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)