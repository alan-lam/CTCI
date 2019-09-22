# Check if a string is a permutation of a palindrome

# Dictionary O(n)
# A palindrome has at most 1 odd count character
def palindromePermutation(check_str):
    d = {}

    for char in check_str:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    found_odd = False
    for char in d:
        if d[char] % 2 == 1:
            if found_odd == True:
                return False
            else:
                found_odd = True
    return True

test_str = input('Enter string: ')
print(palindromePermutation(test_str))

