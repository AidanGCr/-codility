

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

VALUES = {"A" : 1, "C" : 2, "G" : 3, "T" : 4}

def solution(S, P, Q):
    counts = getCounts(S)
    sol = [0] * len(P)
    for i in range(len(P)):
        for base in ["A", "C", "G", "T"]:
            if counts.get(base)[P[i]] != counts.get(base)[Q[i]]:
                sol[i] = VALUES.get(base)
                break
            elif S[P[i]] == base:
                sol[i] = VALUES.get(base)
                break
    return sol


def getCounts(S):
    counts = { "A" : [0], "C" : [0], "G" : [0], "T" : [0]}
    for i in range(len(S)):
        for base in counts.keys():
            if S[i] == base and i == 0:
                counts.update({base : [1]})
            elif S[i] == base and i != 0: 
                new = counts.get(base)
                new.insert(i, counts.get(base)[-1] + 1)
                counts.update({base : new})
            elif S[i] != base and i == 0:
                continue
            else:
                new = counts.get(base)
                new.insert(i, counts.get(base)[-1])
                counts.update({base : new})
    return counts


