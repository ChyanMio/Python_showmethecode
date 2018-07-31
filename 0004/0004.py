# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:08:31 2018

@author: zhang
"""

from collections import Counter
import re


def create_dir(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            line = re.sub(r'[.?!,""/]', ' ', line)
            datalist.extend(line.strip().split(' '))
    di = Counter(datalist)
    return di

def write_to_file(di, filename):
    with open(filename, 'w') as f:
        for key, value in di.items():
            f.write(key+':'+str(value)+'\n')
        
if __name__ == '__main__':
    di = create_dir('test.txt')
    write_to_file(di, 'result.txt')
    
