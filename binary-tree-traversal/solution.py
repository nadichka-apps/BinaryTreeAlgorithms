"""
Module for Binary Tree Traversals.

This module provides implementations for standard depth-first search (DFS)
traversal techniques: Pre-order, In-order, and Post-order using both
iterative and recursive approaches.
"""

class TreeNode:
    """Represents a single node in a binary tree."""
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    """
    Perform an iterative pre-order traversal (Root, Left, Right).

    Returns a list of node data in the order they were visited.
    """
    cur, stack = node, []
    result = []
    while cur or stack:
        if cur:
            result.append(cur.data)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return result

# In-order traversal
def in_order(node):
    """
    Perform a recursive in-order traversal (Left, Root, Right).

    Returns a list of node data in the order they were visited.
    """
    if not node:
        return []
    else:
        return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    """
    Perform an iterative post-order traversal (Left, Right, Root)
    using a visited-flag stack approach.

    Returns a list of node data in the order they were visited.
    """
    result = []
    if not node:
        return []
    stack = [(node, False)]
    while stack:
        one_node, visited = stack.pop()
        if not one_node:
            continue

        if visited:
            result.append(one_node.data)

        else:
            stack.append((one_node, True))
            stack.append((one_node.right, False))
            stack.append((one_node.left, False))
    return result
