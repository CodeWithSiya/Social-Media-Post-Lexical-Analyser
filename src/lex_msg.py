import ply.lex as lex
import sys

"""
Program which does lexical analysis social media messages and posts.
:author: Siyabonga Madondo
:version: 07/03/2026
"""

# Token Definitions
tokens = [
    'WORD',
    'NUMBER',
    'WHITESPACE',
    'PUNCTUATION',
    'HASHTAG',
    'NAME',
]

# Regular Expressions
t_WORD = r'[A-Za-z]+'
t_NUMBER = r'\d+'
t_WHITESPACE = r'[ \t]+'
t_PUNCTUATION = r'[\.,;!\?]'
t_HASHTAG = r'\#[A-Za-z0#-9]*'
t_NAME = r'@[A-Za-z0-9]+'

# Error Function
def t_error(t):
    character = t.value[0]
    print(f'ILLEGAL,{character}')
    t.lexer.outfile.write(f'ILLEGAL,{character}\n')
    t.lexer.skip(1)

# Input File Handling
input_file = sys.argv[1]
content = ''

with open(input_file, 'r') as file:
    content = file.read()

# Lexer Initialisation
lexer = lex.lex()
lexer.input(content)

# Output File Handling
output_file = input_file.replace(".msg", ".tkn")

with open(output_file, 'w') as file:
    lexer.outfile = file

    while True:
        token = lexer.token()
        if not token:
            break
        print(f"{token.type},{token.value}")
        file.write(f"{token.type},{token.value}\n")