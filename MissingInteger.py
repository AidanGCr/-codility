# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    uniques = sorted(set(A))
    maxVal = uniques[len(uniques) - 1]
    if maxVal > 0:
        minVal = maxVal + 1
        for i in range(len(uniques)):
            if i == 0 and uniques[i] >= 2:
                        return 1
            if uniques[i - 1] != uniques[i] - 1:
                for x in range(uniques[i - 1] + 1, uniques[i]):
                    if x >= 1:
                        return x
        return minVal
    else:
        return 1
