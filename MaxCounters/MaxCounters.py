#example array
arr = [3,4,4,6,1,4,4]

'''
Again as in every problem presented here the main thing is to
watch for the complexity and not go above it, while preserving
the maximum correctness
'''

#auto generated function by codility
def solution(N, A):

    #we use this variable to initialize the counters as list
    counters = [0] * N

    #the maximum value which is reached by one of the couters
    #it is used when we hit the max counter condition
    maxValue = 0
    
    #this incrementation is used when we reach the max counter condition
    #to start counting every counter from the new maximum value if it is
    #not reached already
    firstIncrementedN = 0

    for i in A:
        if i >= 1 and i <= N:
            
            #we check if the counter is less than the max value
            #and the max counter condition has come in power
            #if so we increment the value
            if counters[i - 1] < firstIncrementedN:
                counters[i - 1] = firstIncrementedN + 1
            #if both checks fail then we only increment
            else:
                counters[i - 1] += 1

            #simple check for maximum value
            #this can be achieved with predefined functions
            if counters[i - 1] > maxValue:
                maxValue = counters[i - 1]

        #if the max counters condition is reached we set the
        #new "starting value" for each counter
        elif i ==  N + 1:
            firstIncrementedN = maxValue

    #populate remaining values which have not been coverd
    #by the above conditions
    for j in range(0,N):
        if counters[j] < firstIncrementedN:
            counters[j] = firstIncrementedN

    #result
    return counters
    pass

#print solution
print(solution(5, arr))
