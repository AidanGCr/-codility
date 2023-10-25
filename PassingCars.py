# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    count = 0
    multiple = 0
    for car in range(len(A)):
        if A[car] == 0:
            multiple += 1
        else:
            count += multiple
        if count > 1000000000:
            return -1 
    return count
