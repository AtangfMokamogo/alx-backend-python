#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ This function generates a tuple from a provided key and a value**2

    Args:
        k (str): key
        v (float): value <can be interger or float>

    Returns:
        tuple: A tuple with the key and the square of the value as a float.
    """
    return (k, v ** 2.0)
