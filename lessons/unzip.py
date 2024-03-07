"""Splitting a dictionary into two lists."""
__author__ = "730679888"


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """Return a list of keys from the input."""
    return list(input_dict.keys())


def get_values(input_dict: dict[str, int]) -> list[int]:
    """Return a list of values from the input."""
    return list(input_dict.values())