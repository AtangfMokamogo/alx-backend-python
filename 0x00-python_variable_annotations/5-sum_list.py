#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
import math
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function sums a lsit of floats

    Args:
        input_list (List[float]): a list containing only floats

    Returns:
        float: the sum of input_list
    """
    return math.fsum(input_list)
