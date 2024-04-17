from binarytree import Node
import sys

def isnumber(c):
    return c >= '0' and c <= '9'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        if self.value is not None:
            return f"Token({self.type}, {self.value})"
        else:
            return f"Token({self.type})"

    def __repr__(self):
        return str(self)

def lex(str):
    chars = list(str)
    tokens = []

    i = 0
    while i < len(chars):
        char = chars[i]
        if isnumber(char):
            while (i+1) < len(chars) and isnumber(chars[i+1]):
                i += 1
                char += chars[i]
            tokens.append(Token("number", int(char)))
        elif char == '+' or char == '-' or char == '*' or char == '/':
            tokens.append(Token("op", char))
        elif char == '(':
            tokens.append(Token("open_paren", None))
        elif char == ')':
            tokens.append(Token("close_paren", None))
        else:
            print("Syntax error")
            sys.exit(1)

        i += 1

    return tokens

def parse_expression(tokens):
    token = tokens.pop(0)
    if token.type == "number":
        left = Node(token.value)
        if len(tokens) != 0 and tokens[0].type == "op":
            op = tokens.pop(0)
            right = parse_expression(tokens)
            return Node(op.value, left, right)
        else:
            return left
    elif token.type == "open_paren":
        inside = parse_expression(tokens)
        assert tokens.pop(0).type == "close_paren" 
        if len(tokens) != 0 and tokens[0].type == "op":
            op = tokens.pop(0)
            right = parse_expression(tokens)
            return Node(op.value, inside, right)
        else:
            return inside
    else:
        print("Syntax error")
        sys.exit(1)

def infix_to_tree(str):
    lexed = lex(str)
    return parse_expression(lexed)

if __name__ == '__main__':
    print(infix_to_tree(input("Enter the infix expression: ")))

# Grammar
# expression := number {op expression} | open_paren expression close_paren {op expression}
# op := + | - | * | /
# number := [0-9]+
# open_paren := (
# close_paren := )
