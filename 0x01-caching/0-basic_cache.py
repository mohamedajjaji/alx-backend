#!/usr/bin/env python3
"""
Task 0 module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents an object facilitating the storage
    and retrieval of items from a dictionary
    """
    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by its key
        """
        return self.cache_data.get(key, None)
