# Replace all spaces in a string with "%20"

# Loop through each character O(n)
def replaceSpace_1(s):
    return_str = ''

    for char in s:
        if char != ' ':
            return_str += char
        else:
            return_str += '%20'

    return return_str

test_str = input('Enter string: ')
print(replaceSpace_1(test_str))

