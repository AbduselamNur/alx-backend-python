#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait n seconds and return random number between 0 and max_delay"""
    tasks = []
    delays = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
