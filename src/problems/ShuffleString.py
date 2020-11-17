# https://leetcode.com/problems/shuffle-string/

def restoreString(s, indices):
    """
    Given a string s and an integer array indices of the same length.
    The string s will be shuffled such that the character at the ith position 
    moves to indices[i] in the shuffled string. Return the shuffled string.
    """
    output = ["" for ele in range(len(s))]
    for index, ele in enumerate(s):
        output[indices[index]] = ele
    return "".join(output)
