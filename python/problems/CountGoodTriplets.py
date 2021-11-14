# https://leetcode.com/problems/count-good-triplets/

from itertools import combinations as combo 

def countGoodTriplets(arr, a, b, c):
    """
    Given an array of integers arr, and three integers a, b and c. 
    You need to find the number of good triplets.
    A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
        0 <= i < j < k < arr.length
        |arr[i] - arr[j]| <= a
        |arr[j] - arr[k]| <= b
        |arr[i] - arr[k]| <= c
    Where |x| denotes the absolute value of x.
    Return the number of good triplets.i
    """
    counter = 0
    for triplet in combo(arr, 3):
        if abs(triplet[0] - triplet[1]) <= a and abs(triplet[1] - triplet[2]) \
            <= b and abs(triplet[0] - triplet[2]) <= c:
            counter += 1
    return counter
