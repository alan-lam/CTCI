# Check if a string is a permutation of a palindrome

# Dictionary O(N)
# Palindrome has at most 1 odd count character
def palindromePermutation(s):
    d = {}
    odd = 0
    for c in s:
        if d.get(c) is None:
            d[c] = 1
        else:
            d[c] += 1
    for x in d:
        if d[x] % 2 == 1:
            odd += 1
        else:
            if odd > 0:
                odd -= 1
    if odd < 2:
        return True
    return False

s = input()
print(palindromePermutation(s))

