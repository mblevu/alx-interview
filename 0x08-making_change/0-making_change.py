#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make change
    for a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): Total amount to make change for.

    Returns:
        int: Minimum number of coins needed to make change for the total.
        Returns -1 if change cannot be made.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1
    if total != 0:
        return -1
    return num_coins
