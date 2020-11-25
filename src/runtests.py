import os, json, sys
from problems.TwoSum import twoSum
from problems.CountGoodTriplets import countGoodTriplets
from problems.DestinationCity import destCity
from problems.DefangingIPAddress import defangIPaddr
from problems.HeightChecker import heightChecker
from problems.ShuffleString import restoreString
from problems.ShuffleArray import shuffle
from problems.RunningSum import runningSum 
from problems.SumOfAllOddLengthSubarrays import sumOddLengthSubarrays

funcs = {
    "TwoSum": twoSum,
    "CountGoodTriplets": countGoodTriplets,
    "DestinationCity": destCity,
    "DefangingIPAddress": defangIPaddr,
    "HeightChecker": heightChecker,
    "ShuffleString": restoreString,
    "ShuffleArray": shuffle,
    "RunningSum": runningSum,
    "SumOfAllOddLengthSubarrays": sumOddLengthSubarrays
}

def runTest(params, func, tc):
    """
    Desc: runs and returns func with the correct number of params
    """
    if params == 1:
        return func(tc.get("p1"))
    elif params == 2:
        return func(tc.get("p1"), tc.get("p2"))
    elif params == 3:
        return func(tc.get("p1"), tc.get("p2"), tc.get("p3"))
    else:
        return func(tc.get("p1"), tc.get("p2"), tc.get("p3"), tc.get("p4"))


# test the problem and report the results 
passed = 0
prob = sys.argv[1]
if (prob + '.py') in os.listdir('problems'):
    print("Testing " + prob + ":")
    with open('testcases/' + prob + '.json','r') as tcFile:
        tcData = json.load(tcFile)
    numParams = tcData[prob][0].get("param")
    for i in range(tcData[prob][0].get("tests")):
        testcase = tcData[prob][i+1]
        if runTest(numParams, funcs[prob], testcase) == testcase.get("output"):
            print("  Running test " + str(i+1) + " ... Passed")
            passed += 1
        else: 
            print("  Running test " + str(i+1) + " ... Failed")
    print("Passed " + str(passed) + " of " + str(tcData[prob][0].get("tests")))   
else:
    print("The problem: " + prob + " does not exist.")

os.system("py3clean .") 
