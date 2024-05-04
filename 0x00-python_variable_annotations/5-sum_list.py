#!/usr/bin/env python3
'''
type-annotated function
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    takes list of float and reture summed value 
    '''
    return float(sum(input_list))
