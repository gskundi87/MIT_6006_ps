# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 00:07:24 2022

@author: p4u1
"""

import random
import bst

items = [random.randrange(100) for i in range(25)]

tree = bst.bst()

for item in items:
    tree.insert(item)

print(tree)