n = int(input())
n += 1
while len(set(str(n))) < len(str(n)):
    n += 1
print(n)