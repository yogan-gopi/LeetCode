class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        l, r = 0, len(s)-1
        
        while l <= r:
            if res[l] in "aeiouAEIOU":
                while res[r] not in "aeiouAEIOU":
                    r -= 1
                
                res[l], res[r] = res[r], res[l]
                r-=1
            l += 1
        return "".join(res)
                