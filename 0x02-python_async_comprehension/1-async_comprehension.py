#!/usr/bin/env python3
"""
    Asynchronous Python module that takes no arguments and returns a generator
    object that will yield a random number between 0 and 10 every 1 second.
    The generator will loop 10 times. Use the random module.

"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        Coroutine will collect 10 random numbers using an async comprehensing
        over async_generator, then return the list of the 10 random numbers.
    """
    return [num async for num in async_generator()]
