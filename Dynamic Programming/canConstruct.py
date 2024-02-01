def can_construct(target, word_bank, memo=None):
    if memo is None:
        memo = dict()
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in word_bank:
        if target.startswith(word):
            if can_construct(target[len(word):], word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateBoard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee']))
