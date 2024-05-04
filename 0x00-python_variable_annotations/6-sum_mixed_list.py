#!/usr/bin/env python3
'''
type-annotated function
'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    takes mixed list return float
    '''
    return (sum(mxd_lst))
