def insertion_sort(a_list):
    for i in range(len(a_list)):
        j = i
        while j > 0 and a_list[j] < a_list[j-1]:
            a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            j -= 1
    return a_list


def insertion_sort_reversed(a_list):
    for i in range(len(a_list)-1, -1, -1):
        j = i
        while j < len(a_list)-1 and a_list[j] < a_list[j+1]:
            a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
            j += 1
    return a_list[::-1]


def insertion_sort_old(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i+1] < a_list[i]:
            a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
            for j in range(i, 0, -1):
                if a_list[j] < a_list[j-1]:
                    a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
                else:
                    break
    return a_list
