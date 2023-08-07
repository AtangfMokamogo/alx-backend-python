#!/usr/bin/env python3
""" Script that implements Asynchronous Programming in Python """

import asyncio
import random
import time

delay_wait = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """Returns time between intervals"""
    start_time = time.time()

    asyncio.run(delay_wait(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_task = total_time / n
    return average_time_per_task


if __name__ == "__main__":
    n = 5
    max_delay = 10
    avg_time_per_task = measure_time(n, max_delay)
