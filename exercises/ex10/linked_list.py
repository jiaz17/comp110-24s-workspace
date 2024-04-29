"""Utility functions for working with Linked Lists."""

from __future__ import annotations

__author__ = "730679888"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

    def head(self) -> int:
        """Return the data attribute for the first element."""
        return self.data

    def tail(self) -> Node | None:
        """Return list minus the head."""
        return self.next

    def last(self) -> int:
        """Return the last element."""
        current = self
        while current.next is not None:
            current = current.next
        return current.data

def value_at(head: Node | None, index: int) -> int:
	raise IndexError("Index is out of bounds on the list.")