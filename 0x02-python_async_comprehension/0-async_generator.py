#!/usr/bin/env python3
"""
    Asynchronous Python
    Task 0 - Async Generator module that takes no arguments and returns a generator
    object that will yield a random number between 0 and 10 every 1 second.
    The generator will loop 10 times. Use the random module.

"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''yeild a random number at 1sec interval
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
