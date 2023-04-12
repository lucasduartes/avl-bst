#!/usr/bin/env python
import pandas as pd

def load_csv():
    cols = ['Open Time', 'Close']
    df = pd.read_csv('bitcoin.csv', usecols=cols)
    df = df.dropna()
    row_count = len(df)
    return df.tail(row_count//30)
