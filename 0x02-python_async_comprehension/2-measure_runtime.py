#!/usr/bin/env python3
"""
Asynchronous Python module that takes no arguments and returns a generator
object that will yield a random number between 0 and 10 every 1 second.
The generator will loop 10 times. Use the random module.

"""
from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        Coroutine will execute async_comprehension four times in parallel
        using asyncio.gather(). It will then measure the total runtime and
        return it.
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
