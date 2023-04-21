#!/usr/bin/env python
from bintrees import BinaryTree
from load_csv import load_csv
from time import time

df = load_csv() # load timeseries
print('Total instants:', len(df))

def time_bst(df):
    print('BST TEST')
    bst = BinaryTree() # init BST
    print('#'*20)
    print('Timing writing')
    t0 = time()
    time_to_insert_seconds = []
    for _, instant, usd in df.itertuples():
        tn = time()
        bst.insert(instant, usd)
        t = time()
        time_to_insert_seconds += [t - tn]
    tf = time()
    total_time_write = tf - t0
    average_insertion_time = sum(time_to_insert_seconds)/len(time_to_insert_seconds)
    print('#'*20)
    print('Timing reading')
    time_to_read_seconds = []
    sample_count = len(df)//2
    sample_instants = list(df.sample(sample_count)['Open Time'])
    t0 = time()
    for sample_instant in sample_instants:
        tn = time()
        bst.get(sample_instant)
        t = time()
        time_to_read_seconds += [t - tn]
    tf = time()
    total_time_read = tf - t0
    average_read_time = sum(time_to_read_seconds)/len(time_to_read_seconds)
    return average_insertion_time, total_time_write, average_read_time, total_time_read
