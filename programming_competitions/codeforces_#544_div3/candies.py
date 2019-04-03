n, k = map(int, input().split(" "))
d = list(map(int, input().split()))
d.sort()



# dic = {}
# for i in range(n):
#     if d[i] not in dic:
#         dic[d[i]] = 1
#     else:
#         dic[d[i]] += 1
# ct = 0
# print(dic)
# for j in range(n-1, -1, -1):
#     c = d[j] + ? / k
#     if c.is_integer():
#         c = int(c)
#         if c in dic and dic[c] >= 1:
#             print(c, d[j])
#             ct += 2
#             dic[c] -= 1
#             dic[d[j]] -= 1
# print(ct)
