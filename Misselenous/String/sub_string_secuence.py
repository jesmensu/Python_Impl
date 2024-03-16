def isSubsequence(s: str, t: str) -> bool:
        index_s = 0
        index_t = 0
        while index_t<len(t):
            if index_s == len(s):
                return True
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1
        if index_s == len(s):
            return True
        return False

print(isSubsequence("a", "b"))