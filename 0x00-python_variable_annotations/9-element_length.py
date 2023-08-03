#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function calculates the length of each element in the input list

    Args:
        lst (List[str]): a list of strings

    Returns:
        List[Tuple[str, int]]: A list of tuples
    """
    return [(i, len(i)) for i in lst]
