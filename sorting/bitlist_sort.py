def bitlist_sort(data):
    return_array = []
    largest_number = data[0]
    for i in range(1, len(data)):
        if data[i] > largest_number:
            largest_number = data[i]
    b_list = [0]*largest_number
    for j in range(0, len(data)):
        index = data[j] - 1
        b_list[index] += 1
    for k in range(0, len(b_list)):
        if b_list[k] != 0:
            return_array.append(k + 1)
    return return_array
