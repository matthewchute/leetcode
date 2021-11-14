# https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(address):
    """
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
    """
    output = []
    for ele in address:
        if ele == '.':
            output.append('[.]')
        else: 
            output.append(ele)
    return "".join(output)
