# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    seenVals = {}
    for i in range(len(A)):
        if seenVals.get(A[i]) != None:
            seenVals.update({A[i] : seenVals.get(A[i]) + 1})
        else:
            seenVals.update({A[i] : 1})
    return len(seenVals.keys())
