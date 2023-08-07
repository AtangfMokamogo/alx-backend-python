#!/usr/bin/env python3
""" Script that implements Asynchronous Programming in Python """

import asyncio
import random


async def wait_random(max_delay: (int) = 10) -> float:
    """This Function implements an asynchronous coroutine
        that waits for a random time

    Args:
        max_delay (int, optional): the max wait time. Defaults to 10.

    Returns:
        float: the random wait time value
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time


async def main():
    """ The program entry point """
    for _ in range(5):
        random_wait_time = await wait_random()
asyncio.run(main())
