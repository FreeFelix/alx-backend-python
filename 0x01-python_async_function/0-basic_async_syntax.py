#!/usr/bin/env python3
'''
Asyncronos Python function that takes an integer argument and returns a float
   
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    An asynchronous coroutine that takes in an integer argument (max_delay)
    named max_delay (default value: 10) that waits for a random delay between 0
    and max_delay (included and float value) seconds and eventually returns it.

    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return (wait)
