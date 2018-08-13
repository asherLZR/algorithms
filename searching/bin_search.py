def alg_bin_search(a_list, target):
    lo, hi = 0, len(a_list)
    while lo < hi-1:
        mid = (lo + hi)//2
        if target >= a_list[mid]:
            lo = mid
        else:
            hi = mid
    if len(a_list) > 0 and a_list[lo] == target:
        return lo
    else:
        return -1


def repeat(a_list, target):
    lo, hi = 0, len(a_list)-1
    found = -1
    while lo <= hi:
        mid = (lo + hi)//2
        if target == a_list[mid]:
            found = mid
            hi = mid - 1
        elif target < a_list[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return found


def iterative_search(a_list, target):
    if not a_list:
        return -1
    if target is None:
        for i in range(len(a_list)):
            if a_list[i] is None:
                return i
        return -1
    lo, hi = 0, len(a_list)
    stored_mid = None
    while lo < hi:
        mid = (hi + lo) // 2
        if a_list[mid] == target:
            stored_mid = mid
            hi = mid
        elif target < a_list[mid]:
            hi = mid
        else:
            lo = mid + 1
    if stored_mid is not None:
        return stored_mid
    return -1


def search(a_list, target):
    if not a_list:
        return -1
    # None does not divide our search space so the worst case is O(N)
    if target is None:
        for i in range(len(a_list)):
            if a_list[i] is None:
                return i
        return -1
    return search_aux(a_list, target, 0, len(a_list))


def search_aux(a_list, target, lo, hi):
    # len(a_list) == 5, lo == 5, hi == 5 gives mid == 5 (out of range)
    # lo == 4, hi == 5 gives mid == 4
    if lo >= hi:
        return -1
    mid = (lo+hi)//2
    if a_list[mid] is None:
        left = search_aux(a_list, target, lo, mid)
        if left != -1:
            return left
        else:
            return search_aux(a_list, target, mid+1, hi)
    elif a_list[mid] == target:
        # the target may not the first duplicate, so search for a lower one
        if mid != lo:
            earlier_found = search_aux(a_list, target, lo, mid)
            if earlier_found != -1:
                return earlier_found
        return mid
    elif target < a_list[mid]:
        return search_aux(a_list, target, lo, mid)
    else:
        return search_aux(a_list, target, mid+1, hi)
