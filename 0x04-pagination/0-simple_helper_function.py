#!/usr/bin/env python3
"""Function named index_range that takes two integer arguments page and
page_size"""


def index_range(page, page_size):
    """Given a page number and a page size, return the start and end index of
    the page

    Args:
        page (int): The page number
        page_size (int): The number of items you want to display per page

    Returns:
        Tuple[int, int]: A tuple of the start and end index of the page.
    """
    start_index = (page-1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
