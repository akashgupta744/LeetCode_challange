def maxLengthBetweenEqualCharacters(s):
    first_index = [-1] * 26

    max_length = -1

    for i, c in enumerate(s):
        index = ord(c) - ord('a')
        if first_index[index] == -1:
            first_index[index] = i
        else:
            max_length = max(max_length, i - first_index[index] - 1)

    return max_length

s='abca'
print(maxLengthBetweenEqualCharacters(s))