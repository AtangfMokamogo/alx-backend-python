#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ This function safely retrieves the first element of a list

    Parameters:
        lst (list): The input list of unknown element types.

    Returns:
        Union[None, object]: first element of the list if exists, else None
    """
    if lst:
        return lst[0]
    else:
        return None
