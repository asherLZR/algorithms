x = ["a", "b", "a"]
xor_sum = 0
for i in range(0, len(x)):
    xor_sum = xor_sum ^ ord(x[i])
print(chr(xor_sum))
