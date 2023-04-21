#!/usr/bin/env python
from bintrees import AVLTree
from time import time

def time_avl(df):
    print('AVL TEST')
    avl = AVLTree()
    print('#'*20)
    print('Timing writing')
    t0 = time()
    time_to_insert_seconds = []
    for _, instant, usd in df.itertuples():
        tn = time()
        avl.insert(instant, usd)
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
        avl.get(sample_instant)
        t = time()
        time_to_read_seconds += [t - tn]
    tf = time()
    total_time_read = tf - t0
    average_read_time = sum(time_to_read_seconds)/len(time_to_read_seconds)
    return average_insertion_time, total_time_write, average_read_time, total_time_read, time_to_insert_seconds

