import ply.lex as lex

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #### Not used in this problem.
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

states = (
        ('comment', 'exclusive'),
)

def t_comment(t):
    r'\/\*'
    t.lexer.begin('comment')

def t_comment_end(t):
    r'\*\/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    pass

def t_comment_error(t):
    t.lexer.skip(1)

def t_eolcomment(t):
    r'//.*'
    pass

t_ANDAND       = r'&&'
t_COMMA        = r','
t_DIVIDE       = r'/'
t_EQUALEQUAL   = r'=='
t_EQUAL        = r'='
t_LPAREN       = r'\('
t_LBRACE       = r'{'
t_RBRACE       = r'}'
t_SEMICOLON    = r';'
t_MINUS        = r'-'
t_NOT          = r'!'
t_OROR         = r'\|\|'
t_PLUS         = r'\+'
t_RPAREN       = r'\)'
t_TIMES        = r'\*'
t_LE           = r'<='
t_LT           = r'<'
t_GT           = r'>'
t_GE           = r'>='

def t_FALSE(t):
    r'false'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_VAR(t):
    r'var'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z_]*'
    return t

def t_NUMBER(t):
    r'-?[0-9]+\.?[0-9]*'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'"(?:[^"\\]|(?:\\.))*"'
    t.value = t.value[1 : -1]
    return t

t_ignore         = ' \t\v\r'
t_comment_ignore = ' \t\v\r'

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print("JavaScript Lexer: Illegal character " + t.value[0])
        t.lexer.skip(1)


lexer = lex.lex()

#Test
def test_lexer(input_string):
    lexer.input(input_string)
    result = [ ]
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type]
    return result

def test_lexer2(input_string):
    lexer.input(input_string)
    result = [ ]
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type,tok.value]
    return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print(test_lexer(input1) == output1)

input2 = """
if // else mystery
=/*=*/=
true /* false
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print(test_lexer(input2) == output2)

input3 = 'some_identifier -12.34 "a \\"escape\\" b"'
output3 = ['IDENTIFIER', 'some_identifier', 'NUMBER', -12.34, 'STRING',
'a \\"escape\\" b']
print(test_lexer2(input3) == output3)


input4 = '-12x34'
output4 = ['NUMBER', -12.0, 'IDENTIFIER', 'x', 'NUMBER', 34.0]
print(test_lexer2(input4) == output4)

input5 = '0x159'
output5 = ['NUMBER', 0.0, 'IDENTIFIER', 'x', 'NUMBER', 159.0]
print(test_lexer2(input5) == output5 )
