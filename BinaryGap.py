# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    if N >= 4: 
        binary = ""
        binary = getBinary(N, binary)

        maxGap = 0
        localGap = 0
        prevIsOne = False

        for i in range(len(binary)): 
            if binary[i] == "0" and prevIsOne == True:
                localGap = 1
                prevIsOne = False
            elif binary[i] == "0" and prevIsOne == False:
                localGap = localGap + 1
                prevIsOne = False
            elif binary[i] == "1" and prevIsOne == False:
                if localGap > maxGap:
                    maxGap = localGap
                prevIsOne = True
            else:
                prevIsOne = True
        return maxGap
    else:
        return 0

def getBinary(N, currentBinary): 
    if N > 1: 
        currentBinary = getBinary(N // 2, currentBinary)
    nextValue = str(N % 2)
    currentBinary = currentBinary + nextValue
    return currentBinary
