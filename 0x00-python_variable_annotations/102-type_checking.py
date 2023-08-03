#!/usr/bin/env python3
""" This is an implementation of basic type annotations in Python """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Abstract implementation of the zoom feature

    Args:
        lst (Tuple): array of zoom ranges
        factor (int, optional): zooming factor. Defaults to 2.

    Returns:
        List: list of zoom positions
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
