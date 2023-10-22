# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#Note: Too easy hahaha, thanks Esteban lmao

def solution(A):
    xor = 0
    for i in A: 
        xor = xor ^ i
    return xor
