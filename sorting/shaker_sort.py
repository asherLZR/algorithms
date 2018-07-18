# Cocktail Shaker Sort (variant of bubble sort) -> O(n^2)
def cocktail_shaker(a_list):
    swapped = False
    lo = 0
    hi = len(a_list) - 1
    while not swapped:
        for j in range(lo, hi):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                swapped = True
        if not swapped:
            break
        hi -= 1
        swapped = False
        for j in range(hi, lo, -1):
            if a_list[j] < a_list[j - 1]:
                a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
                swapped = True
        lo += 1
        if not swapped:
            break
        else:
            swapped = False
    return a_list
