# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

def sumOddLengthSubarrays(arr):
    """
    Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
    A subarray is a contiguous subsequence of the array.
    Return the sum of all odd-length subarrays of arr.
    """
    output = 0
    oddNum = 1
    while oddNum <= len(arr):
        for i in range((len(arr) - oddNum + 1)):
            output += sum(arr[i:i+oddNum])
        oddNum += 2
    return output
