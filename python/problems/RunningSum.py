# https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(nums):
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i]).
    Return the running sum of nums.
    """
    output = [nums[0]]
    for i in range(1, len(nums)):
        output.append(output[i-1] + nums[i])
    return output
