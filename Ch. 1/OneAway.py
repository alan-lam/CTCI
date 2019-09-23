# Check if one string is one edit away from another string

# Loop through each character O(n)
def oneAway(str_1, str_2):
    if abs(len(str_1) - len(str_2)) > 1:
        return False

    if len(str_1) == len(str_2):
        return checkReplace(str_1, str_2)
    elif len(str_1) < len(str_2):
        return checkOneEdit(str_1, str_2)
    else:
        return checkOneEdit(str_2, str_1)

    return False

def checkReplace(str_1, str_2):
    index = 0
    found_difference = False

    while index < len(str_1):
        if str_1[index] != str_2[index]:
            if found_difference == True:
                return False
            found_difference = True
        index += 1

    return True

# assume str_1 is shorter than str_2
def checkOneEdit(str_1, str_2):
    index_1 = 0
    index_2 = 0
    found_difference = False

    while index_1 < len(str_1):
        if str_1[index_1] != str_2[index_2]:
            if found_difference == True:
                return False
            found_difference = True
            index_2 += 1
        else:
            index_1 += 1
            index_2 += 1
    return True

test_str_1 = input('Enter string: ')
test_str_2 = input('Enter string: ')
print(oneAway(test_str_1, test_str_2))

