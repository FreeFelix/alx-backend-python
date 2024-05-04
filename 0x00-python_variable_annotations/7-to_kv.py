#!/usr/bin/env python3
'''
type-annotated function
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    uses union and accept str , int por float to return tuplue
    '''
    return (k, float(v**2))
