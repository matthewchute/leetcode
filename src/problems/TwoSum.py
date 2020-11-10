# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    """
    Desc: Given an array of integers nums and an integer target, return indices 
    of the two numbers such that they add up to target. You may assume that 
    each input would have exactly one solution, and you may not use the same 
    element twice. You can return the answer in any order.
    """
    compliments = {} 
    for index, number in enumerate(nums):
        compliment = target - number
        if compliment not in compliments:
            compliments[number] = index
        else:
            return [compliments[compliment], index]
