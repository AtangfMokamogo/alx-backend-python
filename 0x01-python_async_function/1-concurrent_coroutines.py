#!/usr/bin/env python3
""" Script that implements Asynchronous Programming in Python """

import asyncio
from typing import List

delay_wait = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    wait_times = await asyncio.gather(*(delay_wait(max_delay) for _ in range(n)))
    return sorted(wait_times)
