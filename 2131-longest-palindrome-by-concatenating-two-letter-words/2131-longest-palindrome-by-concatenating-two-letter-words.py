class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = collections.Counter(words)
        res = 0
        odd = 0
        
        for i in c.keys():
            if i[0] == i[1]:
                res += (c[i]//2)*2*2
                odd = max(odd, (c[i]%2)*2)
            elif i[0] < i[1]:
                res += min(c[i], c[i[::-1]])*2*2
        return res+odd