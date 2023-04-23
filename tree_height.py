#!/usr/bin/env python

def get_tree_height(tree):
    if tree._root is None:
        return 0
    
    stack = [(tree._root, 1)]
    max_height = 0
    
    while stack:
        node, height = stack.pop()
        if node is not None:
            max_height = max(max_height, height)
            stack.append((node.left, height + 1))
            stack.append((node.right, height + 1))
    
    return max_height
