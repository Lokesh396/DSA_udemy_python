def all_construct(target, word_bank, memo=None):
    if memo is None:
        memo = dict()
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            remainder = target[len(word):]
            suffix_ways = all_construct(remainder, word_bank, memo)
            target_ways = suffix_ways
            for way in target_ways:
                way.insert(0, word)
                result.append(way)
    memo[target] = result
    return result


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(all_construct('aaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))