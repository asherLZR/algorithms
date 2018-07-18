n = int(input())
string = list(input())
divisors = []
for i in range(1, n+1):
    if n % i == 0:
        divisors.append(i-1)
for divisor in divisors:
    rev = string[:divisor+1]
    rev = rev[::-1]
    string = rev + string[divisor+1:]
    # print(string)
print("".join(string))
