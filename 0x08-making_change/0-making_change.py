#!/usr/bin/python3
"""Making change problem"""


def makeChange(coins, total):
    """making change as total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n_coins = 0  # number of coins to complete change (total)

    for coin in coins:
        if total % coin < total:
            n_coins += total // coin
            total = total % coin

    return n_coins if total == 0 else -1
