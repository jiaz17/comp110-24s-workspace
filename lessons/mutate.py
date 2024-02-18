"""Mutating functions."""


__author__ = "730679888"


def manual_append(list_input: list[int], value: int) -> None:
    """Mutate its input appending the int parameter to the end of the list[int] parameter."""
    list_input.append(value)


def double(list_input: list[int]) -> None:
    """Mutate its input by multiplying every element in the list[int]."""
    index = 0
    while index < len(list_input):
        list_input[index] *= 2
        index += 1