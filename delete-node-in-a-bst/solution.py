"""
Module for Binary Search Tree (BST) operations.

This module provides a solution for deleting a node from a BST while
maintaining the tree's structural properties. It includes the logic
for handling nodes with zero, one, or two children.
"""
class TreeNode:
    """Represents a single node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Class containing methods to manipulate Binary Search Trees.
    """
    def deleteNode(self, root, key: int):
        """
        Deletes a node with the specified key from a Binary Search Tree (BST).

        Args:
            root (Optional[TreeNode]): The root of the BST.
            key (int): The value to be removed from the tree.

        Returns:
            Optional[TreeNode]: The root of the tree after deletion.
        """
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root
