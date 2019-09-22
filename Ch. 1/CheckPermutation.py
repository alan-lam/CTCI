# Check if one string is a permutation of another

# Sort O(n log n)
def checkPermutation_1(s1, s2):
    if len(s1) != len(s2):
        return False
    t1 = sorted(s1)
    t2 = sorted(s2)
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True

# Dictionary O(n)
def checkPermutation_2(s1, s2):
    if len(s1) != len(s2):
        return False

    d = {}

    for char in s1:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    for char in s2:
        if char in d:
            if d[char] == 0:
                return False
            d[char] -= 1
        else:
            return False
    return True

s1 = input('Enter string: ')
s2 = input('Enter string: ')
print(checkPermutation_1(s1, s2))
print(checkPermutation_2(s1, s2))

