#!/usr/bin/env python3
'''
Asyncronous Python function that takes an integer argument and returns a list
of float values in ascending order of their respective delay times. The function
takes in two integer arguments: n and max_delay. n is the number of times the
function will be called and max_delay is the maximum value of the delay time.

'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Finds the total time for the function to run n times in seconds. The function
    takes in two integer arguments: n and max_delay. n is the number of times the
    function will be called and max_delay is the maximum value of the delay time.
    
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start)/n
