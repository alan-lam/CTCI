# Check if a string has unique characters

# dictionary O(n)
def unique_1(check_str):
    freq_dict = {}
    
    for char in check_str:
        if char in freq_dict:
            return False
        else:
            freq_dict[char] = 1
    return True

# sort O(n log n)
def unique_2(check_str):
    sorted_str_list = sorted(check_str)

    for i in range(len(sorted_str_list)-1):
        if sorted_str_list[i] == sorted_str_list[i+1]:
            return False
    return True

test_str = input('Enter string: ')
print(unique_1(test_str))
print(unique_2(test_str))

