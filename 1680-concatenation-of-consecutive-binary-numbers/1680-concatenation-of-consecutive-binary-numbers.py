class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bits, res, MOD = 1, 0, 10**9 + 7
        for x in range(1, n + 1):
            res = ((res << bits) + x) % MOD
            if x == (1 << bits) - 1:
                bits += 1    
        return res