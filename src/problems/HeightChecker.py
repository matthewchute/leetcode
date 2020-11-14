# https://leetcode.com/problems/height-checker/

def heightChecker(heights):
    """
    Students are asked to stand in non-decreasing order of heights for an annual photo.
    Return the minimum number of students that must move in order for all students to be 
    standing in non-decreasing order of height. Notice that when a group of students is 
    selected they can reorder in any possible way between themselves and the non selected 
    students remain on their seats.
    """
    counter = 0
    sortedHeights = sorted(heights)
    for i in range(len(heights)):
        if sortedHeights[i] != heights[i]:
            counter += 1
    return counter        
