#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
from typing import TypeVar, Dict, Union


k = TypeVar('k')
v = TypeVar('v')


def safely_get_value(dct: Dict[k, v], key: k,
                     default: v = None) -> Union[v, None]:
    """ This function safely retrieves a value from a dictionary.

    Parameters:
        dct (Dict[k, v]): The input dictionary.
        key (k): The key to retrieve the value.
        default (v, optional): default value to return if the key is not found

    Returns:
        Union[v, None]: value corresponding to the key if found else default
    """
    if key in dct:
        return dct[key]
    else:
        return default
