import copy

def power_set(partial, s):
    a.append(copy.deepcopy(partial))
    for i in range(s, len(nums)):
        partial.append(nums[i])
        power_set(partial, i + 1)
        partial.pop()


a = []
nums = list(map(int, input().split()))
power_set([], 0)
print(a)