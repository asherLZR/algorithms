def heaps(a_list, n):
    if n == 1:
        print(a_list)
    else:
        for i in range(0, n-1):
            heaps(a_list, n - 1)
            if n % 2 == 0:
                a_list[i], a_list[n - 1] = a_list[n - 1], a_list[i]
            else:
                a_list[0], a_list[n - 1] = a_list[n - 1], a_list[0]
        heaps(a_list, n - 1)


def alt_heaps(a_list, n):
    # the original orientation of the list
    if n == len(a_list):
        print(a_list)
    # if the subset is greater than 2 items, continue breaking it down
    if n > 1:
        # leave the last character of the list unchanged and generate permutations for the rest
        alt_heaps(a_list, n - 1)
    # for character except the last character
    for i in range(0, n-1):
        # if the subset is divisible by 2, put element in last position
        if n % 2 == 0:
            a_list[i], a_list[n - 1] = a_list[n - 1], a_list[i]
            print(a_list)
        # if n is indivisible by 2,
        else:
            a_list[0], a_list[n - 1] = a_list[n - 1], a_list[0]
            print(a_list)

        # if the subset is greater than 2 items, continue breaking it down
        # at the base case, i = 1,
        if n > 2:
            alt_heaps(a_list, n - 1)


def permute(a_list, count=0):
    if count == len(a_list):
        print(a_list)
    else:
        for i in range(count, len(a_list)):
            a_list[count], a_list[i] = a_list[i], a_list[count]
            permute(a_list, count + 1)
            a_list[count], a_list[i] = a_list[i], a_list[count]


L = ['a', 'b', 'c', 'd']

permute(L)
