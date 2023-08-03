#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function creates a method that multiplies a value

    Args:
        multiplier (float): multiplier

    Returns:
        Callable[[float], float]: A function that multiplies a value
    """
    def product_func(x: float) -> float:
        return x * multiplier

    return product_func
