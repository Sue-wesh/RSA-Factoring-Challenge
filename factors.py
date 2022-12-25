#!/usr/bin/python3

import sys
import ctypes
from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def sys_time(function):
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()


    return "\nreal: {}\nuser: {}\nsys: {}".format(
            end_time - start_time, 
            end_resources.ru_utime - start_resources.ru_utime, 
            end_resources.ru_stime - start_resources.ru_stime)

def division(n: int) -> int:
    while n % 2 == 0:
        return 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            return f
        else:
            f += 2

    return 1

def prime_factors():

    with open(sys.argv[1], 'r') as prime:
        line = prime.readline()
        while line != '':
            n = int(line)
            rep = division(n)
            print("{} = {} x {}".format(n, n//rep, rep))

            line = prime.readline()
