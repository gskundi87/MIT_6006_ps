# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:52:14 2022

@author: p4u1
"""

import bst

class avl(bst.bst):
    def insert(self, key):
        if self.root is None:
            self.root = bst.node(value=key)
            self.root.height = 0
            self.root.tree_size = 1
            return self.root

        current = self.root
        p = None

        while current is not None:
            p = current
            if key is current.value:
                return None
            elif key < current.value:
                current  = current.left
            else:
                current  = current.right

        current = bst.node(value=key, parent=p)

        if key < p.value:
            p.left = current
        else:
            p.right = current
        
        self.rebalance(current)
        
        return current
    
    def delete(self, key):
        pass

    def delete_node(self, node):
        pass
    
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        self.update_node_height(x)
        self.update_node_height(y)
        self.update_node_tree_size(x)
        self.update_node_tree_size(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        self.update_node_height(x)
        self.update_node_height(y)
        self.update_node_tree_size(x)
        self.update_node_tree_size(y)
        
    def rebalance(self, node):
        while node is not None:
            self.update_node_height(node)
            self.update_node_tree_size(node)
            if self.node_height(node.left) >= 2 + self.node_height(node.right):
                if self.node_height(node.left.left) >= self.node_height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif self.node_height(node.right) >= 2 + self.node_height(node.left):
                if self.node_height(node.right.right) >= self.node_height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent