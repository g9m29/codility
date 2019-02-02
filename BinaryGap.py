def solution(N):
    # write your code in Python 3.6
    binaryGapLength = 0
    maxBinaryGapLength = 0
    shouldCount = False

    if ((N == 1) or (N == 2) or (N == 3)):
        return 0

    while N > 0:
        previousDigit = N % 2
        N = N // 2
        currentDigit = N % 2

        if ((currentDigit == 0) and (previousDigit != 0)):
            shouldCount = True

        if (shouldCount and (previousDigit == 0)):
            shouldCount = True

        if ((currentDigit != 0) and (previousDigit) == 0):
            shouldCount = False

            if (maxBinaryGapLength < binaryGapLength):
                maxBinaryGapLength = binaryGapLength

            binaryGapLength = 0;

        if shouldCount:
            binaryGapLength += 1

    return maxBinaryGapLength
    pass

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(1041))
