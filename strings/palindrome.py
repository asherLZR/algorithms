def palindrome(s):
    i = 0
    j = len(s)-1

    while i < len(s)//2:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

print(palindrome("abcvba"))
