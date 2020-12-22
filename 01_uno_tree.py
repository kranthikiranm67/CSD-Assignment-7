"""
Uno Tree
Given a binary tree root, return whether all values in the tree are the same.

For example, given

   3
  / \
 3   3
    / \
   3   3
  / \
 3   3
Return true

Given,

   3
  / \
 3   4
Return false.

Example 1
Input
root = {val: 870, left: {val: 870, left: {val: 870, left: None, right: None}, right: None},right: {val: 870, left: {val: 870, left: None, right: None}, right: None}}

Output
True

Explanation
Every node has the value 870

Example 2
Input
root = {val: 862, left: {val: 862, left: {val: 862, left: None, right: None}, right: None},
    right: {val: 862, left: {val: 9000, left: None, right: None}, right: None}}

Output
False

Explanation
There is a node with a value 9000 while others are 862
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


def uno_tree(root):
    # write your code here
    


# DO NOT TOUCH THE BELOW CODE
class TestUnoTree(unittest.TestCase):

    def test_01(self):
        root = trees.create_from_string(
            '{val: 870, left: {val: 870, left: {val: 870, left: None, right: None}, right: None}, right: {val: 870, left: {val: 870, left: None, right: None}, right: None}}')
        self.assertEqual(uno_tree(root), True)

    def test_02(self):
        root = trees.create_from_string(
            '{val: 862, left: {val: 862, left: {val: 862, left: None, right: None}, right: None}, right: {val: 862, left: {val: 9000, left: None, right: None}, right: None}}')
        self.assertEqual(uno_tree(root), False)

    def test_03(self):
        root = trees.create_from_string(
            '{val: 34, left: None, right: None}')
        self.assertEqual(uno_tree(root), True)

    def test_04(self):
        root = trees.create_from_string(
            '{val: 148, left: {val: 148, left: {val: 148, left: {val: 148, left: None, right: None}, right: {val: 148, left: None, right: None}}, right: None}, right: {val: 148, left: {val: 148, left: None, right: None}, right: None}}')
        self.assertEqual(uno_tree(root), True)

    def test_05(self):
        root = trees.create_from_string(
            '{val: 148, left: {val: 148, left: {val: 148, left: {val: 148, left: {val: 148, left: {val: 148, left: None, right: None}, right: {val: 148, left: None, right: None}}, right: {val: 148, left: None, right: None}}, right: {val: 148, left: {val: 18, left: None, right: None}, right: None}}, right: {val: 148, left: None, right: None}}, right: {val: 148, left: {val: 148, left: {val: 148, left: None, right: None}, right: None}, right: {val: 148, left: None, right: {val: 148, left: None, right: None}}}}')
        self.assertEqual(uno_tree(root), False)

    def test_06(self):
        root = trees.create_from_string(
            '{val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: {val: 1111, left: None, right: None}}}, right: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}, right: {val: 1111, left: None, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}}}}')
        self.assertEqual(uno_tree(root), True)

    def test_07(self):
        root = trees.create_from_string(
            '{val:1}')
        self.assertEqual(uno_tree(root), True)

    def test_08(self):
        root = trees.create_from_string(
            '{val: 4325, left: {val: 4325, left: {val: 4325, left: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: {val: 4325, left: {val: 4325, left: None, right: None}, right: {val: 4325, left: {val: 4325, left: None, right: {val: 4325, left: None, right: None}}, right: {val: 4325, left: None, right: None}}}}, right: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: None}, right: None}, right: None}}, right: {val: 4325, left: {val: 4325, left: None, right: None}, right: {val: 4325, left: None, right: None}}}, right: {val: 4325, left: {val: 4825, left: None, right: None}, right: None}}, right: {val: 4325, left: None, right: None}}, right: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: None}, right: None}, right: {val: 4325, left: None, right: {val: 4325, left: {val: 4325, left: {val: 4325, left: None, right: None}, right: {val: 4325, left: None, right: {val: 4325, left: None, right: {val: 4325, left: None, right: None}}}}, right: {val: 4325, left: {val: 4325, left: None, right: None}, right: None}}}}}')
        self.assertEqual(uno_tree(root), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
