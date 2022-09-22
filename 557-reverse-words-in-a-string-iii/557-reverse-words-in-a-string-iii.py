class Solution:
    def reverseWords(self, s: str) -> str:
        def helper(s):
            n = len(s)
            stri = ""
            for i in range(n-1, -1, -1):
                stri += s[i]
            return stri
        s = s.split()
        res = ""
        for i in s:
            res += helper(i)
            res += " "
        return res.rstrip(res[-1])