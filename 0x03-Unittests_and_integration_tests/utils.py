#!/usr/bin/env python3
"""
Generic utilities for GitHub organization client.
"""

import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]

def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a value in a nested dictionary using a sequence of keys.

    Parameters
    ----------
    nested_map : Mapping
        A nested dictionary.
    path : Sequence
        A sequence of keys representing the path to the value.

    Returns
    -------
    Any
        The value found at the specified path in the nested dictionary.

    Raises
    ------
    KeyError
        If a key in the path does not exist in the dictionary.

    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map

def get_json(url: str) -> Dict:
    """
    Fetch JSON data from a remote URL.

    Parameters
    ----------
    url : str
        The URL to fetch the JSON from.

    Returns
    -------
    Dict
        The JSON data retrieved from the URL.
    """
    response = requests.get(url)
    return response.json()

def memoize(fn: Callable) -> Callable:
    """
    Decorator to memoize a method, caching its result after the first call.

    Parameters
    ----------
    fn : Callable
        The method to be memoized.

    Returns
    -------
    Callable
        The memoized method.

    Example
    -------
    >>> class MyClass:
    >>>     @memoize
    >>>     def a_method(self):
    >>>         print("a_method called")
    >>>         return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """Memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
