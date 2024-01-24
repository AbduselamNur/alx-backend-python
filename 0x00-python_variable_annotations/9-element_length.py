#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples, one for each element and its length """
    return [(i, len(i)) for i in lst]
