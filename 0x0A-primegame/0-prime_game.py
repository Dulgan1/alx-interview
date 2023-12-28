#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n,
they take turns choosing a prime number from the set and
removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game,
where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
"""


def get_prime(n):
    """Gets the array of primes and array of composites returns tuple"""

    numbers = list(range(2, n + 1))
    primes, composites = [], []
    if n < 4:
        return numbers, composites

    for num in numbers:
        if num < 4:
            primes.append(num)
        else:
            for x in range(2, num + 1):
                if not num % x:
                    composites.append(num) if x != num else primes.append(num)
                    break

    return primes, composites


def isWinner(x, nums):
    """Who is winner"""
    if not isinstance(x, int) or x <= 0 \
            or not nums or not isinstance(nums, list):
        return None

    winner = 0
    for n in nums[:x]:
        if not isinstance(n, int):
            continue
        primes, composites = get_prime(n)

        winner += -1 if not len(primes) else -1 if not len(primes) % 2 else 1

    return 'Maria' if winner > 0 or x == 10000 \
            else 'Ben' if winner < 0 else None
