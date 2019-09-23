# Compress a string using counts of repeated characters

def compress(s):
    if (len(s)) < 2:
        return s

    index_1 = 0
    index_2 = 1
    return_str = ''
    repeated = 1 # count number of repeated characters

    while index_2 < len(s):
        if s[index_1] == s[index_2]:
            index_2 += 1
            repeated += 1
        else:
            return_str += s[index_1]
            return_str += str(repeated)
            index_1 = index_2
            index_2 += 1
            repeated = 1
        if index_2 == len(s):
            return_str += s[index_1]
            return_str += str(repeated)

    # return original string if no compressions
    if len(return_str) == 2*len(s):
        return s
    return return_str

test_str = input('Enter string: ')
print(compress(test_str))

