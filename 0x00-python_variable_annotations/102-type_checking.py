#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """

from typing import Union


def safe_first_element(lst: list) -> Union[None, object]:
    """ This function safely retrives the first element of a list

    Args:
        lst (list): The input list of unknown element types.

    Returns:
        Union[None, object]: The first element of the list if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
