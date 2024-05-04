#!/usr/bin/env python3
'''
type-annotated function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    multiplier float uses callable from typing
    '''
    return lambda x: x * multiplier
