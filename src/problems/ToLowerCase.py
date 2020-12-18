# https://leetcode.com/problems/to-lower-case/

def toLowerCase(str):
    """
    Implement function ToLowerCase() that has a string parameter str, and 
    returns the same string in lowercase.
    """
    output = []
    for c in str:
        if 65 <= ord(c) <= 90:
            output.append(chr(ord(c) + 32))
        else:
            output.append(c)
    return "".join(output)
