# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    leaves = {}
    for leaf in range(len(A)):
        if leaves.get(str(A[leaf])) == None:
            leaves.update({str(A[leaf]) : leaf})
    if len(list(leaves.keys())) == X: 
        return max(leaves.values())
    return -1


