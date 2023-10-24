# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sumBefore = 0
    sumAfter = 0
    localDif = 2000
    minDif = 2000

    for i in A:
        sumAfter += i
    for i in range(len(A)):
        if i == 0: 
            continue
        else: 
            sumBefore += A[i-1]
            sumAfter -= A[i-1]
            localDif = abs(sumAfter - sumBefore)
        if localDif < minDif:
            minDif = localDif
            
    return minDif


