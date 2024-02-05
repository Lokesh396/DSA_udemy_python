def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[len(string) - 1]:
        return palindrome(string[1:len(string) - 1])
    return False


print(palindrome('maamm'))
