# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Note: For this question I initally lost points for not 
# considering the empty array case.

def solution(A, K):
    if len(A) == 0:
        return A
    else:
        newA = [None] * len(A)
        K = K % len(A)
        for i in range(len(A)):
            if i + K <= len(A) - 1:
                newA[i + K] = A[i]
            else:
                newK = K - (len(A) - i)
                newA[newK] = A[i]
        return newA


