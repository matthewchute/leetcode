# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

def canBeEqual(target, arr):
    """
    Given two integer arrays of equal length target and arr.
    In one step, you can select any non-empty sub-array of arr and reverse it. 
    You are allowed to make any number of steps.
    Return True if you can make arr equal to target, or False otherwise.
    """
    targetDict = {}
    arrDict = {}
    for i in target:
        targetDict[i] = targetDict.get(i, 0) + 1
    for i in arr:
        arrDict[i] = arrDict.get(i, 0) + 1
    return targetDict == arrDict
