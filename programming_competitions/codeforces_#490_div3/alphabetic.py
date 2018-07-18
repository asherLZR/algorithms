n, k = list(map(int, input().split(" ")))
string = list(input())
my_dict = {}
for letter in string:
    if letter in my_dict:
        my_dict[letter] = my_dict[letter] + 1
    else:
        my_dict[letter] = 1

for i in range(ord('a'), ord('z')+1):
    key = chr(i)
    if key not in my_dict:
        continue
    if k <= 0:
        my_dict[key] = 0
    elif my_dict[key] > k:
        my_dict[key] = k
        k -= my_dict[key]
    else:
        k -= my_dict[key]

for letter in string:
    if my_dict[letter] > 0:
        my_dict[letter] -= 1
    else:
        print(letter, end="")
