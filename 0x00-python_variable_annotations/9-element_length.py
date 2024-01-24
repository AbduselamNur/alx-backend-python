#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
