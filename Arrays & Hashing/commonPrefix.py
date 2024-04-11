"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 """


def longestCommonPrefix(strs):
    out = ""
    ll = len(strs)
    min_l = 201
    for i in strs:
        if len(i) < min_l:
            min_l = len(i)

    # print(min_l)

    for i in range(min_l):
        c = 0
        val = strs[0][i]
        for j in strs:
            if j[i] == val:
                c += 1
        if c == ll:
            out += val
        else:
            break

    return out


print(longestCommonPrefix(["flower", "flow", "flight"]))
