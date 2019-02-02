def solution(A, K):
    
    newOrderList = []
    key = K
    
    if len(A) == 0:
        return 0
    
    if len(A) <= K:
        key = K % len(A)
        
    if A[1:] == A[:-1]:
        return A

    for x in A:
        if (key <= (len(A) - 1)):
            newOrderList.insert(key, x)
            key += 1
        else:
            newOrderList.insert(0, x)
            key = 1;
            
    return newOrderList
    pass

print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 1, 2, 3, 5], 7))
