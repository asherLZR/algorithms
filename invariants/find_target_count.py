"""
IV: At the start of each loop, count is the number of occurrences of target in A[0...i-1].

Init: when i = 0, count = 0
# occurrences of target in A[0...i-1] = # in A[0...-1] = # in [] = 0
as required

Maintenance:
Assume IV holds at the start of the loop where i = k. We want to show IV holds at the start
of the loop where i = k+1.
    2 Cases:
        A[k] = target
        count will be incremented
        Since by assumption, count was # of occurrences of target in A[0...k-1], count will now
        be # occurrences in A[0...k] as required

        A[k] != target
        count will not be incremented
        Since by assumption, count was # of occurrences of target in A[0...k-1], count will now
        be # occurrences in A[0...k] as required

Since IV holds at the start of each loop it holds when i = n, count = # occurrences in A[0...n]
"""

def count_target(a_list, target):
    count = 0
    i = 0
    while i < len(a_list):
        if a_list[i] == target:
            count += 1
        i += 1
    return count
