#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """


def add(a: float, b: float) -> float:
    """This computes the sum of two floats

    Args:
        a (float): float 1
        b (float): float 2

    Returns:
        float: sum of floats a and b
    """
    return a + b
