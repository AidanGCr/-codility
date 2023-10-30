# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    highestVals = [float("-inf")] * 3
    for i in range(len(A)):
        if A[i] > highestVals[0]:
            highestVals[2] = highestVals[1]
            highestVals[1] = highestVals[0]
            highestVals[0] = A[i]
        elif A[i] > highestVals[1]:
            highestVals[2] = highestVals[1]
            highestVals[1] = A[i] 
        elif A[i] > highestVals[2]:
            highestVals[2] = A[i]
    return highestVals[0] * highestVals[1] * highestVals[2]
