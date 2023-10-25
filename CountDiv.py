# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    factorsInA = 0
    if not A % K: 
        factorsInA = (A - 1) // K
    else:
        factorsInA = A // K 
    return B // K - factorsInA
