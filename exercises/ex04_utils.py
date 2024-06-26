"""Ex04_Utils."""
__author__ = "730679888"


def all(int_list: list[int], single_int: int) -> bool:
    """Bool test indicated number."""
    if len(int_list) == 0:
        return False
    for item in int_list:
        if item != single_int:
            return False
    return True


def max(input_list: list[int]) -> int:
    """Return the largest number in the list."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    largest = input_list[0]
    for number in input_list:
        if number > largest:
            largest = number
    
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determination if every element at every index is equal in both lists."""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Appending values to first list."""
    for element in list2:
        list1.append(element)