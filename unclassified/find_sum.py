test_list = [3, 10, 4, 9, 8, 7]
target = 12

# naive O(N^2)
for i in range(len(test_list)):
    current = test_list[i]
    complement = target - current
    for j in range(i+1, len(test_list)):
        if test_list[j] == complement:
            print(current, complement)

print()

# improved O(N log N), assuming unique values
test_list = sorted(test_list)
i, j = 0, len(test_list)-1
while i < j:
    current = test_list[i]
    complement = test_list[j]
    if target - current == complement:
        print(current, complement)
        i += 1
        j -= 1
    elif target - current > complement:
        i += 1
    else:
        j -= 1
