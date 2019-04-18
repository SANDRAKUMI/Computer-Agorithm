def max_subarray(A):
    max_ending_here = A[0]
    startOld = start = end = max_so_far = 0
    for i, x in enumerate(A[1:], 1):
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            start = i + 1
        elif max_ending_here == max_so_far:
            startOld = start
            end = i
    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print ("Starting Index %d"%(startOld)) 
    print ("Ending Index %d"%(end))
    
A = input('Enter the list of numbers: ')
A = A.split()
A = [int(x) for x in A]
print ("Number of items in the array = ", len(A))
max_subarray(A)

