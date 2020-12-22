"""
This is a helper class to create & print Trees
Needed to run other tree programs
"""

# DO NOT TOUCH THE CODE IN THIS FILE
# If you would like to play around copy this code to another file

import json


class Tree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # Tree String
        return self.tree_string(self)

    def __repr__(self):
        # Represents Tree
        return str(self.val)

    def tree_string(self, tree, level=0):
        """ Actual Tree String Implementation """

        if tree != None:
            root_str = "   " * level + str(tree.val) + "\n"
            left_str = "   " * (level + 1) + \
                self.tree_string(tree.left, level + 1) + "\n"
            right_str = "   " * (level + 1) + \
                self.tree_string(tree.right, level + 1) + ""

            return root_str + left_str + right_str
        return "   " * level + 'None'

    def __eq__(self, other):
        # Two Tree Comparions for Equality
        if self is None and other is None:
            return True

        if self is not None and other is not None:
            return (self.val == other.val) and self.left.__eq__(other.left) and self.right.__eq__(other.right)

        return False


def create_from_dict(data):
    """Create Tree From Dictionary"""

    new_tree = Tree(int(data["val"]))

    if data.get("left") is not None:
        new_tree.left = create_from_dict(data["left"])

    if data.get("right") is not None:
        new_tree.right = create_from_dict(data["right"])

    return new_tree


def create_from_string(root_str):
    """Create Tree From String"""

    root_dict = root_str.replace(' ', '').replace(',left:None', '').replace(',right:None', '').replace(
        'val:', '"val":').replace('left:', '"left":').replace('right:', '"right":')

    data = json.loads(root_dict)

    return create_from_dict(data)
