# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sumFull = 0
    sumA = 0
    for i in range(len(A)):
        sumA = sumA + A[i]
        sumFull = sumFull + i
    sumFull = sumFull + 2*(len(A)) + 1
    return sumFull - sumA
