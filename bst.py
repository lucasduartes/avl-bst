#!/usr/bin/env python
import numpy as np
import pandas as pd
from bintrees import BinaryTree
from load_csv import load_csv
from time import time

df = load_csv() # load timeseries

bst = BinaryTree() # init AVL

t0 = tn = time()

time_to_insert_seconds = []

for _, instant, usd in df.itertuples():
    bst.insert(instant, usd)
    tn = time()
    t = time()
    time_to_insert_seconds += [t - tn]
    tn = t

tf = time()

total_time = tf - t0
average_insertion_time = sum(time_to_insert_seconds)/len(time_to_insert_seconds)
print(time_to_insert_seconds)
print('Average insertion time:', average_insertion_time)
print('Total insertion time:', total_time)
print('Total instants:', len(time_to_insert_seconds))
