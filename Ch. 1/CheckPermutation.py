# Check if one string is a permutation of another

# Sort O(N log N)
def checkPermutation_1(s1, s2):
    if len(s1) != len(s2):
        return False
    t1 = "".join(sorted(s1))
    t2 = "".join(sorted(s2))
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True

# Dictionary O(N)
def checkPermutation_2(s1, s2):
    if len(s1) != len(s2):
        return False
    d = {}
    for i in range(len(s1)):
        if d.get(s1[i]) is None:
            d[s1[i]] = 1
        else:
            d[s1[i]] += 1
    for i in range(len(s2)):
        if d.get(s2[i]) is None or d.get(s2[i]) == 0:
            return False
        else:
            d[s2[i]] -= 1
    return True

s1 = input()
s2 = input()
print(checkPermutation_1(s1, s2))
print(checkPermutation_2(s1, s2))

