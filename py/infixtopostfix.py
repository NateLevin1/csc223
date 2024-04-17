from infixtotree import infix_to_tree

def infix_to_postfix(str):
    tree = infix_to_tree(str)
    return postfix_expression(tree)

def postfix_expression(tree):
    if tree.left is not None and tree.right is not None: # if is not leaf...
        return f"{postfix_expression(tree.left)} {postfix_expression(tree.right)} {tree.value}"
    else:
        return tree.value

if __name__ == '__main__':
    print(infix_to_postfix("3+4*2"))
