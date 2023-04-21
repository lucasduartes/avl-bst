#!/usr/bin/env python
from avl import time_avl
from bst import time_bst
from load_csv import load_csv
import matplotlib.pyplot as plt

df = load_csv()
average_insertion_time_avl, total_time_write_avl, average_read_time_avl, total_time_read_avl = time_avl(df)
average_insertion_time_bst, total_time_write_bst, average_read_time_bst, total_time_read_bst = time_bst(df)

fig, axs = plt.subplots(2, 2)
axs[0, 0].bar(['AVL', 'BST'], [total_time_write_avl, total_time_write_bst])
axs[0, 0].set_title('Total insertion time (seconds)')
axs[0, 1].bar(['AVL', 'BST'], [average_insertion_time_avl, average_insertion_time_bst])
axs[0, 1].set_title('Average insertion time (seconds)')
axs[1, 0].bar(['AVL', 'BST'], [total_time_read_avl, total_time_read_bst])
axs[1, 0].set_title('Total read time (seconds)')
axs[1, 1].bar(['AVL', 'BST'], [average_read_time_avl, average_read_time_bst])
axs[1, 1].set_title('Average read time (seconds)')
plt.tight_layout()
plt.savefig('comparação.png')
