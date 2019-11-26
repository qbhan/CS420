import ply.lex as lex

# List of token names. This is always required
tokens = [

    'NUMBER',
    'ID',

    # operators
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'INCREMENT',

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
    'FOR',

    # types
    'INT',
    'FLOAT',
    'POINTER'
]

# Regular expression rules
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_INCREMENT = r'\++'

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


t_IF = r'if'
t_FOR = r'for'

t_INT = r'int'
t_FLOAT = r'float'
# t_POINTER = r'*'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

    # Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)


t_ignore = ' \t'


# def t_if(t):
#     r'if'
#     return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input("a + if asjioeifw")

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
