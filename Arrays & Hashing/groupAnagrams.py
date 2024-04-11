"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
 original letters exactly once.
"""


def groupAnagrams(strs):
    memo = {}
    for i in range(len(strs)):
        word = sorted(strs[i])
        word = "".join(word)
        if word in memo:
            memo[word].append(strs[i])
        else:
            memo[word] = [strs[i]]
    output = []
    for key, values in memo.items():
        output.append(values)
    return output


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
