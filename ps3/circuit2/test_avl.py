# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:37:14 2022

@author: p4u1
"""
import random
import avl

items = [random.randrange(100) for i in range(25)]

tree = avl.avl()

for item in items:
    tree.insert(item)

print(tree)
