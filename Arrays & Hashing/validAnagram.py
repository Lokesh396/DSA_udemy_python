"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
 original letters exactly once
"""
import collections


# Approach 1 O(nlgn)

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    if s == t:
        return True
    return False


# Approach 2 O(n)


def isValidAnagram(s, t):
    if len(s) != len(t):
        return False
    c1 = collections.Counter(s)
    c2 = collections.Counter(t)
    return c1 == c2


str1 = "nagaram"
str2 = "anagram"

print(isValidAnagram(str1, str2))
print(isAnagram(str1, str2))
