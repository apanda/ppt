#!/usr/bin/env python3
import sys
sys.path.insert(0, "/Users/apanda/code/python-prompt-toolkit")
from prompt_toolkit import prompt
from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.layout.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer
from prompt_toolkit.history import FileHistory
history = FileHistory('.cerebro')

our_style = style_from_dict({
    Token.Comment:   '#bbbbbb bold',
    Token.Keyword:   '#888888 bold',
})

def run_cmd(cmd):
    #print('Running: %s' % answer)
    from subprocess import call
    if not cmd:
        return True
    if cmd == 'exit':
        return False
    try:
        call(cmd.split(' ' ))
    except:
        print(":(")
    return True

if __name__ == '__main__':
    while True:
        try:
            answer = prompt('cerebro % ', multiline=True, lexer=PygmentsLexer(
                SqlLexer), style=our_style, history=history)
            if not run_cmd(answer):
                break
        except EOFError as e:
            print("You typed ctrl-d. exiting")
            break
        except KeyboardInterrupt as e:
            continue
