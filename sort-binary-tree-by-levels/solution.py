"""
Module for Level-Order Tree Traversal.

This module provides functionality to traverse a binary tree level by level
(Breadth-First Search), returning node values in a flattened list format.
"""
class Node:
    """Represents a single node in a binary tree."""
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
def tree_by_levels(node):
    """
    Perform a level-order traversal (Breadth-First Search) of the tree.

    This function traverses the tree level by level, from top to bottom
    and left to right, returning a flat list of node values.
    """
    if node is None:
        return []
    queue = [node]
    next_queue = []
    level = []
    result = []
    while queue != []:
        next_queue = []
        for node in queue:
            level.append(node.value)
            if node.left is not None:
                next_queue.append(node.left)
            if node.right is not None:
                next_queue.append(node.right)
        result.extend(level)
        level = []
        queue = next_queue
    return result
