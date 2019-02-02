def solution(A):
    # write your code in Python 3.6
        
    A.sort()
        
    if len(A) == 1:
        return A[0]

    for x in range(0, len(A) - 1, 2):
        if ((A[x] != A[x+1]) and (A[x]) != None):
            return A[x]

    return A[len(A)-1]
    
    pass
    
print(solution([9,3,9,3,9,7,9]))
