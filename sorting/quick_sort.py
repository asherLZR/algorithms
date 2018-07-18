def quick_sort(a_list):
    return quick_sort_aux(a_list, 0, len(a_list))


def quick_sort_aux(a_list, lo, hi):
    if lo < hi:
        a_list, pivot = partition(a_list, lo, hi)
        quick_sort_aux(a_list, lo, pivot)
        quick_sort_aux(a_list, pivot+1, hi)     # pivot+1 since pivot is in the right place
    return a_list


def partition(a_list, lo, hi):
    pivot_chosen = (lo+hi)//2   # choose the pivot from the middle of the list
    # bring the pivot to the end of the list
    a_list[pivot_chosen], a_list[hi-1] = a_list[hi-1], a_list[pivot_chosen]
    pivot_index = lo
    # for each value up to the value before the pivot, move smaller values to the left of the pivot index
    # increment pivot index by one after
    for i in range(lo, hi-1):
        if a_list[i] < a_list[hi-1]:
            a_list[pivot_index], a_list[i] = a_list[i], a_list[pivot_index]
            pivot_index += 1
    a_list[pivot_index], a_list[hi-1] = a_list[hi-1], a_list[pivot_index]
    return a_list, pivot_index
