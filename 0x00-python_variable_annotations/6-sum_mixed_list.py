#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """


from typing import List


def sum_mixed_list(mxd_lst: List[float]) -> float:
    """ this function calculate the sum of a list of integers and floats

    Args:
        mxd_lst (List[float]): A list of integers and floats

    Returns:
        float: The sum of mxd_lst
    """
    return sum(mxd_lst)
