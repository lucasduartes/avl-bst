#!/usr/bin/env python
from bintrees import BinaryTree, AVLTree
from load_csv import load_csv
from time_tree import time_tree
import matplotlib.pyplot as plt

df = load_csv()
avl = AVLTree()
bst = BinaryTree()
(average_insertion_time_avl, 
 total_time_write_avl, 
 average_read_time_avl, 
 total_time_read_avl, 
 time_to_insert_seconds_avl, 
 height_avl) = time_tree(df, avl)

(average_insertion_time_bst, 
 total_time_write_bst, 
 average_read_time_bst, 
 total_time_read_bst, 
 time_to_insert_seconds_bst, 
 height_bst) = time_tree(df, bst)

fig, axs = plt.subplots(2, 3, figsize=(12,10))
axs[0, 0].bar(['AVL', 'BST'], [total_time_write_avl, total_time_write_bst])
axs[0, 0].set_title('Total insertion time')
axs[0, 1].bar(['AVL', 'BST'], [average_insertion_time_avl, average_insertion_time_bst])
axs[0, 1].set_title('Average insertion time')
axs[1, 0].bar(['AVL', 'BST'], [total_time_read_avl, total_time_read_bst])
axs[1, 0].set_title('Total read time')
axs[1, 1].bar(['AVL', 'BST'], [average_read_time_avl, average_read_time_bst])
axs[1, 1].set_title('Average read time')
axs[0, 2].plot(time_to_insert_seconds_avl)
axs[0, 2].set_title('Time to insert (AVL)')
axs[1, 2].plot(time_to_insert_seconds_bst)
axs[1, 2].set_title('Time to insert (BST)')
plt.suptitle('Time units are in seconds', fontsize=10, x=0.95, y=0.013, ha='right')
plt.tight_layout()
plt.savefig('comparação.png')
