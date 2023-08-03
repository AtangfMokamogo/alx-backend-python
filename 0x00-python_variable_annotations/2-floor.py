#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
import math


def floor(n: float) -> int:
    """This computes the floor of a float

    Args:
        n (float): a float

    Returns:
        int: an interger repesenting the floor of the float provided
    """
    return math.floor(n)
