# https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    """
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    """
    output = []
    for i in range(n):
        output.append(nums[i])
        output.append(nums[n+i])
    return output
