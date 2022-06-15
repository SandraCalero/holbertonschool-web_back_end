#!/usr/bin/env python3
"""Paginate a database of popular baby names
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """The function returns a list of lists, where each list is a row of
        data

        Args:
            page (int, optional):  The page number to return, defaults to 1
            page_size (int, optional): The number of items to return per page,
            defaults to 10.

        Returns:
            List[List]: A list of lists.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        gp_range = index_range(page, page_size)
        gp_start = gp_range[0]
        gp_end = gp_range[1]
        return self.dataset()[gp_start:gp_end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        It takes a page number and a page size, and returns a dictionary with
        the page data, the page number, the page size, the next page number,
        the previous page number, and the total number of pages

        Args:
            page (int, optional): The page number to return, defaults to 1.
            page_size (int, optional): The number of items to return per page,
            defaults to 10

        Returns:
            Dict: A dictionary with the following keys:
            page_size: The length of the returned dataset page
            page: The current page number
            data: The dataset page (equivalent to return from previous task)
            next_page: Number of the next page, None if no next page
            prev_page: Number of the previous page, None if no previous page
            total_pages: The total number of pages in the dataset as an integer
        """
        page_data = self.get_page(page, page_size)
        data_size = len(self.dataset())
        total_pages = math.ceil(data_size / page_size)
        info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages
        }

        return info
