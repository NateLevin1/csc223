#
#  A red-black tree satisfies the following properties:
#   1) Red/Black Property: Every node is colored, either red or black.
#   2) Root Property: The root is black.
#   3) Leaf Property: Every leaf (None) is black.
#   4) Red Property: If a red node has children then, the children are always black.
#   5) Depth Property: For each node, any simple path from this node to any of its descendant leaf has the same black-depth (the number of black nodes).
#
# (from https://www.programiz.com/dsa/red-black-tree)

from binarytree import Node

class RBNode(Node):
    def __init__(self, value, color):
        super().__init__(value)
        self.color = color
        self.parent = None
        self.value = str(value) + color[0]

    def set_red(self):
        self.color = "RED"
        self.value = self.value[:-1] + "R"

    def set_black(self):
        self.color = "BLACK"
        self.value = self.value[:-1] + "B"

    def get_value(self):
        return int(self.value[:-1])


# Implementation is translated from the ideas in https://www.eecs.umich.edu/courses/eecs380/ALG/niemann/s_rbt.txt
   
class RedBlackTree():
    def __init__(self):
        self.root = None

    # visualization: https://www.programiz.com/dsa/red-black-tree#:~:text=Left%20Rotate
    def rotateLeft(self, x):
        y = x.right

        # establish x.right link
        x.right = y.left
        if (y.left != None): y.left.parent = x

        # establish y.parent link
        if (y != None): y.parent = x.parent
        if (x.parent):
            if (x == x.parent.left):
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self.root = y

        # link x and y
        y.left = x
        if (x != None): x.parent = y

    # visualization: https://www.programiz.com/dsa/red-black-tree#:~:text=Right%20Rotate
    def rotateRight(self, x):
        y = x.left

        # establish x.left link
        x.left = y.right
        if (y.right != None): y.right.parent = x

        # establish y.parent link
        if (y != None): y.parent = x.parent
        if (x.parent):
            if (x == x.parent.right):
                x.parent.right = y
            else:
                x.parent.left = y
        else:
            self.root = y

        # link x and y
        y.right = x
        if (x != None): x.parent = y


    # maintain the red-black tree properties after inserting a node
    def insertFixup(self, x):
        # check Red-Black properties
        while (x != self.root and x.parent and x.parent.color == "RED"):
            # violation!
            if (x.parent == x.parent.parent.left):
                y = x.parent.parent.right
                if (y and y.color == "RED"):
                    # uncle is RED
                    x.parent.set_black()
                    y.set_black()
                    x.parent.parent.set_red()
                    x = x.parent.parent
                else:
                    # uncle is BLACK
                    if (x == x.parent.right):
                        # make x a left child
                        x = x.parent
                        self.rotateLeft(x)

                    # recolor and rotate
                    x.parent.set_black()
                    x.parent.parent.set_red()
                    self.rotateRight(x.parent.parent)
            else:
                # mirror image of above code
                y = x.parent.parent.left
                if (y and y.color == "RED"):
                    # uncle is RED
                    x.parent.set_black()
                    y.set_black()
                    x.parent.parent.set_red()
                    x = x.parent.parent
                else:
                    # uncle is BLACK
                    if (x == x.parent.left):
                        x = x.parent
                        self.rotateRight(x)
                    x.parent.set_black()
                    x.parent.parent.set_red()
                    self.rotateLeft(x.parent.parent)
        self.root.set_black()

    # will call insertFixup after inserting
    def insert(self, value):
        # find where node belongs
        current = self.root
        parent = 0
        while (current != None):
            # prevent duplicates (as they mess up a RB tree)
            if (value == current.get_value()): return (current)
            parent = current
            current = current.left if value < current.get_value() else current.right

        # setup new node
        x = RBNode(value, "RED")
        x.parent = parent

        # insert node in tree
        if(parent):
            if(value < parent.get_value()):
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x

        self.insertFixup(x)
        return(x)

    def print(self):
        print(self.root)


if __name__ == "__main__":
    tree = RedBlackTree()

    while True:
        user_input = input("Enter a number to add to tree: ")
        try:
            int(user_input)
        except:
            print("No number provided, exiting.")
            break
        tree.insert(int(user_input))
        tree.print()

