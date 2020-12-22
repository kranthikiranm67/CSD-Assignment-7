"""
Elephant Tree
Given the root of a binary tree root, return the same tree 
except every node's value is replaced by its original value 
plus all of the sums of its left and right subtrees.

For example, given

   0
  / \
 1   2
    / \
   1   0
  / \
 3   2
Return

   9
  / \
 1   8
    / \
   6   0
  / \
 3   2

Example 1
Input
root = {val: 2, left: {val: 1, left: {val: 0, left: None, right: None}, right: None}, right: {val: 4, left: {val: 3, left: None, right: None}, right: None}}

Output
{val: 10, left: {val: 1, left: {val: 0, left: None, right: None}, right: None}, right: {val: 7, left: {val: 3, left: None, right: None}, right: None}}

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



def elephant_tree(root):
    #write your code here


# DO NOT TOUCH THE BELOW CODE
class TestElephantTree(unittest.TestCase):

    def test_01(self):
        root_01 = trees.create_from_string(
            '{val: 2, left: {val: 1, left: {val: 0, left: None, right: None}, right: None}, right: {val: 4, left: {val: 3, left: None, right: None}, right: None}}')
        elephant_tree_01 = trees.create_from_string(
            '{val: 10, left: {val: 1, left: {val: 0, left: None, right: None}, right: None}, right: {val: 7, left: {val: 3, left: None, right: None}, right: None}}')

        self.assertEqual(elephant_tree(root_01), elephant_tree_01)

    def test_02(self):
        root_02 = trees.create_from_string(
            '{val: 0, left: {val: 1, left: None, right: None}, right: {val: 2, left: {val: 1, left: {val: 3, left: None, right: None}, right: {val: 2, left: None, right: None}}, right: {val: 0, left: None, right: None}}}')
        elephant_tree_02 = trees.create_from_string(
            '{val: 9, left: {val: 1, left: None, right: None}, right: {val: 8, left: {val: 6, left: {val: 3, left: None, right: None}, right: {val: 2, left: None, right: None}}, right: {val: 0, left: None, right: None}}}')

        self.assertEqual(elephant_tree(root_02), elephant_tree_02)

    def test_03(self):
        root_03 = trees.create_from_string(
            '{val: 0, left: {val: 1, left: None, right: None}, right: {val: 2, left: {val: 1, left: {val: 3, left: None, right: {val: 2, left: None, right: None}}, right: None}, right: {val: 0, left: None, right: None}}}')
        elephant_tree_03 = trees.create_from_string(
            '{val: 9, left: {val: 1, left: None, right: None}, right: {val: 8, left: {val: 6, left: {val: 5, left: None, right: {val: 2, left: None, right: None}}, right: None}, right: {val: 0, left: None, right: None}}}')

        self.assertEqual(elephant_tree(root_03), elephant_tree_03)

    def test_04(self):
        root_04 = trees.create_from_string(
            '{val: 0, left: {val: 1, left: None, right: None}, right: {val: 2, left: None, right: None}}')
        elephant_tree_04 = trees.create_from_string(
            '{val: 3, left: {val: 1, left: None, right: None}, right: {val: 2, left: None, right: None}}')
        self.assertEqual(elephant_tree(root_04), elephant_tree_04)

    def test_05(self):
        root_05 = trees.create_from_string(
            '{val: 10, left: None, right: None}')
        elephant_tree_05 = trees.create_from_string(
            '{val: 10, left: None, right: None}')

        self.assertEqual(elephant_tree(root_05), elephant_tree_05)

    def test_06(self):
        root_06 = trees.create_from_string(
            '{val: 148, left: {val: 148, left: {val: 148, left: {val: 148, left: None, right: None}, right: {val: 148, left: None, right: None}}, right: None}, right: {val: 148, left: {val: 148, left: None, right: None}, right: None}}')
        elephant_tree_06 = trees.create_from_string(
            '{val: 1036, left: {val: 592, left: {val: 444, left: {val: 148, left: None, right: None}, right: {val: 148, left: None, right: None}}, right: None}, right: {val: 296, left: {val: 148, left: None, right: None}, right: None}}')

        self.assertEqual(elephant_tree(root_06), elephant_tree_06)

    def test_07(self):
        root_07 = trees.create_from_string(
            '{val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: {val: 1111, left: None, right: None}}}, right: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 1111, left: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}, right: {val: 1111, left: None, right: {val: 1111, left: {val: 1111, left: None, right: None}, right: None}}}}')
        elephant_tree_07 = trees.create_from_string(
            '{val: 24442, left: {val: 16665, left: {val: 14443, left: {val: 11110, left: {val: 8888, left: {val: 4444, left: None, right: {val: 3333, left: {val: 1111, left: None, right: None}, right: {val: 1111, left: None, right: None}}}, right: {val: 3333, left: {val: 2222, left: {val: 1111, left: None, right: None}, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 2222, left: {val: 1111, left: None, right: None}, right: None}}, right: {val: 1111, left: None, right: None}}, right: {val: 6666, left: {val: 2222, left: {val: 1111, left: None, right: None}, right: None}, right: {val: 3333, left: None, right: {val: 2222, left: {val: 1111, left: None, right: None}, right: None}}}}')

        self.assertEqual(elephant_tree(root_07), elephant_tree_07)


if __name__ == '__main__':
    unittest.main(verbosity=2)
