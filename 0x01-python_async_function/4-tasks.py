#!/usr/bin/env python3
'''
Asyncronous Python function that takes an integer argument and returns a list
of float values in ascending order of their respective delay times. The function
takes in two integer arguments: n and max_delay. n is the number of times the
function will be called and max_delay is the maximum value of the delay time.

'''
from typing import List
import asyncio


time_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Return a list of awaited response from previous function in ascending order
    of their respective delay times. The function takes in two integer arguments:
    n and max_delay. n is the number of times the function will be called and
    max_delay is the maximum value of the delay time.
    
    '''
    res = await asyncio.gather(
        *tuple(map(lambda _: time_wait_random(max_delay), range(n)))
    )
    return sorted(res)
