# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    counters = [0] * N
    minVal = 0
    maxVal = 0
    for K in A:
        if 1 <= K <= N:
            if counters[K - 1] < minVal:
                counters[K - 1] = minVal + 1
            else:
                counters[K - 1] = counters[K - 1] + 1
            if counters[K - 1] > maxVal:
                maxVal = counters[K - 1]
        elif K == N + 1:
            minVal = maxVal
    for counter in range(len(counters)):
        if counters[counter] < minVal:
            counters[counter] = minVal
    return counters
