def all_subsets(a):
    n = len(a)
    ans = []
    """ 
    loop over all numbers between [1 or 0(include empty set)] and [2^n-2 or 2^n-1(include itself)] 
    
    1 2 3
    ------ 
    0 0 0
    0 0 1
    0 1 0
    0 1 1
    1 0 0
    1 0 1
    1 1 0
    1 1 1
    
    """
    for mask in range(0, (1 << n)):
        subset = []
        for i in range(n):
            """
            m looks at each row, i looks at each column
            
            (1 << i) gives us ...00100...
            
            (1<<i)&m checks if [row, column] is one or zero
            one means include
            zero means exclude
            
            """
            if ((1 << i) & mask) != 0:
                subset.append(a[i])
        ans.append(subset)
    return ans

print(all_subsets([1, 2, 3, 4]))