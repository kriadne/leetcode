#longest common prefix (LCP)
# cambiar prints por returns para usar en leetcode
def longestCommonPrefix(strs: list[str]) -> str:
    strs.sort()
    FIRST = strs[0]
    LAST = strs[-1]
    count = 0
    for i in range(len(FIRST)):
        if FIRST[i] != LAST[i]: break
        else: count += 1
    if count == 0: print('')
    else: print(FIRST[:count])

longestCommonPrefix(['flower', 'flow', 'flight']) #case ex 