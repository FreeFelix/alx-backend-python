#!/usr/bin/env python3
'''
Asyncronus python function that takes an integer argument and returns a list
of float values in ascending order of their respective delay times.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Return a list of awaited response from previous function in ascending
    order of their respective delay times. The function takes in two integer 
    arguments: n and max_delay. n is the number of times the function will be
    called and max_delay is the maximum value of the delay time.
    
    '''
    res = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(res)
