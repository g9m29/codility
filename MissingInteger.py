# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    aLen = len(A)
    if aLen < 1:
        return 1
        
    if aLen == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    

    A.sort()

    if not(1 in A):
        return 1

    for x in range(0, aLen - 1):
        if (A[x] > 0 and A[x+1] not in range(A[x], A[x] + 2)):
            return A[x] + 1
            
    return A[aLen - 1] + 1
    
    pass
    
print(solution([1,2,3]))
print(solution([-1, -3]))
print(solution([6,3,7]))
print(solution([1, 3, 6, 4, 1, 2]))
