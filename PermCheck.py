# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    values = {}
    for i in range(len(A)):
        if values.get(A[i]) == None:
            values.update({A[i] : 1})
        else: 
            return 0
    if max(values.keys()) > len(A):
        return 0
    return 1
