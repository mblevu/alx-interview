#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """
    determines the fewest number of coins needed to meet a given amount
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
