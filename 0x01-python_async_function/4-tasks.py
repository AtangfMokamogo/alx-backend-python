#!/usr/bin/env python3
""" Script that implements Asynchronous Programming in Python """
import asyncio
from typing import List
delay_wait = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a different implememtation of wait_n func

    Args:
        n (int): number of coroutines to spawn
        max_delay (int): delay in floats

    Returns:
        List[float]: list if wait times for coroutines
    """
    delay_times = await asyncio.gather(*(delay_wait(n, max_delay) for _ in range(n)))
    return sorted(delay_times)
