# https://leetcode.com/problems/coin-change/

""" TODO: Need to return optimal number of coins. """

def coinChange(coins, amount):
    """
    You are given coins of different denominations and a total amount of money amount. 
    Write a function to compute the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    """
    numCoins = 0
    revSortedCoins = sorted(coins, reverse = True)
    if amount == 0:
        return 0
    for coin in revSortedCoins:
        numCoins += amount / coin
        amount = amount % coin
        if amount == 0:
            break
    if amount != 0:
        return -1
    return numCoins
