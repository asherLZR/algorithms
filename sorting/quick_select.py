def partition(a_list, lo, hi, p):
    a_list[p], a_list[hi-1] = a_list[hi-1], a_list[p]
    pivot_index = lo
    for i in range(lo, hi-1):
        if a_list[i] < a_list[hi - 1]:
            a_list[pivot_index], a_list[i] = a_list[i], a_list[pivot_index]
            pivot_index += 1
    a_list[pivot_index], a_list[hi - 1] = a_list[hi - 1], a_list[pivot_index]
    return a_list, pivot_index


def quick_select_aux(a_list, lo, hi, k):
    """
    This algorithm finds the kth smallest element in unsorted a_list. Median of median algorithm gives
    O(N log N) worst case as it returns a pivot if it is within a certain range from the median.

    :complexity: O(N^2) worst case, O(N) average case
    """
    a_list, p = partition(a_list, lo, hi, lo)
    if k < p:
        return quick_select_aux(a_list, lo, p, k)
    elif k > p:
        return quick_select_aux(a_list, p+1, hi, k)
    else:
        return a_list[k]

def quick_select(a_list, k):
    return quick_select_aux(a_list, 0, len(a_list), k)



if __name__ == '__main__':
    for l in range(6):
        print(quick_select([3, 2, 1, 5, 6, 4], l))