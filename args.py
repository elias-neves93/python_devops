#!/usr/bin/python3

# -*- coding: UTF-8 -*-

import argparse

def fib(n):
    a,b = 0, 1
    for i in range(n):
        a,b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num",help="The Fibonacce number you wish to calculate.", type=int)
    args = parser.parse_args()

    result = fib(args.num)
    print ("The {} the fib number is {}".format(str(args.num),str(result)))

if __name__ == '__main__':
    Main()
