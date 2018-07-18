def merge_sort(a_list):
    return merge_sort_aux(a_list, 0, len(a_list))


def merge_sort_aux(a_list, lo, hi):
    if hi - lo < 2:
        return a_list[lo: hi]
    mid = (hi + lo)//2
    return merge(merge_sort_aux(a_list, lo, mid), merge_sort_aux(a_list, mid, hi))


def merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged += left
    merged += right
    return merged
