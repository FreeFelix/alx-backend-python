#!/usr/bin/env python3
'''
Asyncronous Python function that takes an integer argument and returns a task

'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Takes int return asyncio task object. The function takes in an integer argument
    named max_delay and returns a asyncio task object that waits for a random delay
    between 0 and max_delay (included and float value) seconds and eventually returns it.
    
    '''
    return asyncio.create_task(wait_random(max_delay))
