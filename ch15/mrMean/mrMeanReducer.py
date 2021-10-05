#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2011-02-21 15:36:10
LastEditor: John
LastEditTime: 2020-08-12 17:07:06
Discription: 
Environment: 
'''
'''
Created on Feb 21, 2011

@author: Peter
'''
import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.rstrip()
       
input = read_input(sys.stdin)#creates a list of input lines

#split input lines into separate items and store in list of lists
mapperOut = [line.split('\t') for line in input]

#accumulate total number of samples, overall sum and overall sum sq
cumVal=0.0
cumSumSq=0.0
cumN=0.0
for instance in mapperOut:
    nj = float(instance[0])
    cumN += nj
    cumVal += nj*float(instance[1])
    cumSumSq += nj*float(instance[2])
    
#calculate means
mean = cumVal/cumN
meanSq = cumSumSq/cumN

#output size, mean, mean(square values)
print("%d\t%f\t%f" % (cumN, mean, meanSq))
print("report: still alive",file=sys.stderr)