"""
Unival Tree Count
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
The unival trees include 4 leaf nodes (3 of them are 1s, the other one is the rightmost 0), and one subtree in the middle (containing all 1s).

Example 1
Input
root = {val: 0, left: {val: 1, left: None, right: None}, right: {val: 0, left: {val: 1, left: {
    val: 1, left: None, right: None}, right: {val: 1, left: None, right: None}}, right: {val: 0, left: None, right: None}}}

Output
5

Explanation
This is the example used in the description.

Example 2
Input
root = {val: 1, left: {val: 1, left: None, right: None},
    right: {val: 1, left: None, right: None}}

Output
3

Explanation
Each leaf node is a unival subtree and so is the root node.

Example 3
Input

root = {val: 1, left: {val: 0, left: None, right: None},
    right: {val: 0, left: None, right: None}}
Output

2
Explanation

The two leaf nodes are unival trees.

Example 4
Input

root = {val: 1, left: {val: 1, left: None, right: None},
    right: {val: 0, left: None, right: None}}
Output
2

Explanation

Each leaf node is a unival tree.
"""

import helper_trees as trees
import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def unival_tree(root):
    # write your code here


# DO NOT TOUCH THE BELOW CODE
class TestUnivalTree(unittest.TestCase):

    def test_01(self):
        root = trees.create_from_string(
            '{val: 0, left: {val: 1, left: None, right: None}, right: {val: 0, left: {val: 1, left: {val: 1, left: None, right: None}, right: {val: 1, left: None, right: None}}, right: {val: 0, left: None, right: None}}}')

        self.assertEqual(unival_tree(root), 5)

    def test_02(self):
        root = trees.create_from_string(
            '{val: 1, left: {val: 1, left: None, right: None}, right: {val: 1, left: None, right: None}}')

        self.assertEqual(unival_tree(root), 3)

    def test_03(self):
        root = trees.create_from_string(
            '{val: 1, left: {val: 0, left: None, right: None}, right: {val: 0, left: None, right: None}}')

        self.assertEqual(unival_tree(root), 2)

    def test_04(self):
        root = trees.create_from_string(
            '{val: 1, left: {val: 1, left: None, right: None}, right: {val: 0, left: None, right: None}}')

        self.assertEqual(unival_tree(root), 2)

    def test_05(self):
        root = trees.create_from_string(
            '{val: 1, left: None, right: None}')

        self.assertEqual(unival_tree(root), 1)

    def test_06(self):
        root = trees.create_from_string(
            '{val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: {val: 1111, left: None, right: None}}}, right: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}, right: {val: 1111, left: None, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}}}}')

        self.assertEqual(unival_tree(root), 22)

    def test_07(self):
        root = trees.create_from_string(
            '{val: 9, left: {val: 1, left: None, right: None}, right: {val: 8, left: {val: 6, left: {val: 3, left: None, right: None}, right: {val: 2, left: None, right: None}}, right: {val: 0, left: None, right: None}}}')

        self.assertEqual(unival_tree(root), 4)

    def test_08(self):
        root = trees.create_from_string(
            '{val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: {val: 1, left: None, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}, right: None}')

        self.assertEqual(unival_tree(root), 101)

    def test_09(self):
        root = trees.create_from_string(
            '{val: 4325, left: {val: 4325, left: {val: 4325, left: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: {val: 4325, left: {val: 4325, left: None, right: None}, right: {val: 4325, left: {val: 4325, left: None, right: {val: 4325, left: None, right: None}}, right: {val: 4325, left: None, right: None}}}}, right: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: None}, right: None}, right: None}}, right: {val: 4325, left: {val: 4325, left: None, right: None}, right: {val: 4325, left: None, right: None}}}, right: {val: 4325, left: {val: 4825, left: None, right: None}, right: None}}, right: {val: 4325, left: None, right: None}}, right: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: None}, right: None}, right: {val: 4325, left: None, right: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: None}, right: {val: 4325, left: None, right: {val: 4325, left: None, right: {val: 4325, left: None, right: None}}}}, right: {val: 4325, left: {val: 4325, left: None, right: None}, right: None}}}}}')

        self.assertEqual(unival_tree(root), 32)


if __name__ == '__main__':
    unittest.main(verbosity=2)
