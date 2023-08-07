#!/usr/bin/env python3
""" Script that implements Asynchronous Programming in Python """
import asyncio
from asyncio.tasks import ensure_future
delay_wait = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """async tasks lists"""
    return ensure_future(delay_wait(max_delay))


if __name__ == "__main__":
    max_delay = 5
    task = task_wait_random(max_delay)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
