"""Functions that implement sorting algorithms."""


__author__ = "730679888"



def insertion_sort(x: list[int]) -> None:

    """Basic insertion sort algorithm."""

    """Insert into an already sorted list."""

    for idx in range(len(x)):

        min_index = idx

        for j in range(idx + 1, len(x)):

            if x[j] < x[min_index]:

                min_index = j

        x[idx], x[min_index] = x[min_index], x[idx]

    return None



def selection_sort(x: list[int]) -> None:

    """Basic selection sort algorithm."""

    """ Repeatedly find the minimum and swap it."""

    for idx in range(1, len(x)):

        current_element = x[idx]

        j = idx - 1

        while j >= 0 and current_element < x[j]:

            x[j + 1] = x[j]

            j -= 1

        x[j + 1] = current_element

    return None