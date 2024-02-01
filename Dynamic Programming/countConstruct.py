def count_construct(target, word_bank, memo=None):
    if memo is None:
        memo = dict()
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    count = 0
    for word in word_bank:
        if target.startswith(word):
            ways = count_construct(target[len(word):], word_bank, memo)
            count += ways
    memo[target] = count
    return count


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('skateBoard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee']))




