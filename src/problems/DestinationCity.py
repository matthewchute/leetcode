# https://leetcode.com/problems/destination-city/

def destCity(paths):
    """
    You are given the array paths, where paths[i] = [cityAi, cityBi] means 
    there exists a direct path going from cityAi to cityBi. Return the destination 
    city, that is, the city without any path outgoing to another city.
    It is guaranteed that the graph of paths forms a line without any loop, 
    therefore, there will be exactly one destination city.
    """
    departures = [trip[0] for trip in paths]
    destinations = [trip[1] for trip in paths]
    for destination in destinations:
        if destination not in departures:
            return destination
