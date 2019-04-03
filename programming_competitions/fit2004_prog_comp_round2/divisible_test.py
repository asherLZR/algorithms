from fit2004_prog_comp_round2.divisible_substrings import divisible_substrings
from fit2004_prog_comp_round2.divisible_substrings_bruteforce import brute_force
import random

d = 1
result = True
for _ in range(50):
    s = ""
    for _ in range(random.randint(1, 1000)):
        digit = random.randint(1, 9)
        s += str(digit)
    result &= (divisible_substrings(d, s) == brute_force(d, s))
print(result)