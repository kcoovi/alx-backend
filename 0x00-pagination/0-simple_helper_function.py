#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Docstring
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
