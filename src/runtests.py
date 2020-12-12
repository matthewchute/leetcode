import os, json, sys, subprocess

def getFunc(prob):
    """ Desc: import and return func to be tested """
    if prob == "TwoSum":
        from problems.TwoSum import twoSum
        return twoSum
    elif prob == "CountGoodTriplets":
        from problems.CountGoodTriplets import countGoodTriplets
        return countGoodTriplets
    elif prob == "DestinationCity":
        from problems.DestinationCity import destCity
        return destCity
    elif prob == "DefangingIPAddress":
        from problems.DefangingIPAddress import defangIPaddr
        return defangIPaddr
    elif prob == "HeightChecker":
        from problems.HeightChecker import heightChecker
        return heightChecker
    elif prob == "ShuffleString":
        from problems.ShuffleString import restoreString
        return restoreString
    elif prob == "ShuffleArray":
        from problems.ShuffleArray import shuffle
        return shuffle
    elif prob == "RunningSum":
        from problems.RunningSum import runningSum 
        return runningSum
    elif prob == "SumOfAllOddLengthSubarrays":
        from problems.SumOfAllOddLengthSubarrays import sumOddLengthSubarrays
        return sumOddLengthSubarrays
    elif prob == "MakeTwoArraysEqualByReversingSubArrays":
        from problems.MakeTwoArraysEqualByReversingSubArrays import canBeEqual
        return canBeEqual

def getOutput(params, func, tc):
    """ Desc: runs func with the correct num of params and returns output """
    if params == 1:
        return func(tc.get("p1"))
    elif params == 2:
        return func(tc.get("p1"), tc.get("p2"))
    elif params == 3:
        return func(tc.get("p1"), tc.get("p2"), tc.get("p3"))
    else:
        return func(tc.get("p1"), tc.get("p2"), tc.get("p3"), tc.get("p4"))

def runTests():
    """ Desc: test the problem and report the results """
    passed = 0
    problem = sys.argv[1]
    if problem + '.py' in os.listdir('problems'):
        print("Testing " + problem + ":")
        with open('testcases/' + problem + '.json','r') as tcFile:
            tcData = json.load(tcFile)
        numParams = tcData[problem][0].get("param")
        function = getFunc(problem)
        for i in range(tcData[problem][0].get("tests")):
            testcase = tcData[problem][i+1]
            if getOutput(numParams, function, testcase) == testcase.get("output"):
                print("  Running test " + str(i+1) + " ... Passed")
                passed += 1
            else: 
                print("  Running test " + str(i+1) + " ... Failed")
        print("Passed " + str(passed) + " of " + \
            str(tcData[problem][0].get("tests")))   
    else:
        print("The problem: " + problem + " does not exist.")

if __name__ == "__main__":
    runTests()
    subprocess.call("find . -name '*.pyc' -delete", shell = True)
