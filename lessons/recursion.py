"""Define Recursion Function."""



def f(n: int, k: int) -> int:

    """Multiplies two integers n and k using recursion."""

    if n == 0:

        return 0

    else:

        return k + f(n - 1, k)
