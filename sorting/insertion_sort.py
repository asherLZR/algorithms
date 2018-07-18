def insertion_sort(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i + 1] < a_list[i]:
            a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
            for j in range(i, 0, -1):
                if a_list[j] < a_list[j - 1]:
                    a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
                else:
                    break
    return a_list
