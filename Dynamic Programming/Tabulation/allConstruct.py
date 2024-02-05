def all_construct(target, word_bank):
    table = [[]] * (len(target) + 1)
    table[0] = [[]]
    for i in range(len(table)):
        if len(table[i]):
            for word in word_bank:
                if word == target[i:i+len(word)]:
                    ways = []
                    for j in range(len(table[i])):
                        way = [] + table[i][j]
                        way.append(word)
                        ways.append(way)
                    table[i+len(word)] = [] + table[i+len(word)] + ways
    return table[len(target)]


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('aaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))