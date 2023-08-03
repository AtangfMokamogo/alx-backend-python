#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ This function safely retrieves a value from a dictionary.

    Parameters:
        dct (Mapping[Any, T]): The input dictionary.
        key (Any): The key to retrieve the value.
        default (Union[T, None], optional): default value to return

    Returns:
        Union[T, None]: value corresponding to the key if found else default
    """
    if key in dct:
        return dct[key]
    else:
        return default
