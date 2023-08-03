#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """


def concat(str1: str, str2: str) -> str:
    """This concatenates two strings

    Args:
        str1 (str): string 1
        str2 (str): string 2

    Returns:
        str: a concatenated string of str1 and str2
    """
    return str1 + str2
