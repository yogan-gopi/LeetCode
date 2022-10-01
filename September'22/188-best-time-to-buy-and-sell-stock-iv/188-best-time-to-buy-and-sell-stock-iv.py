class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k <= 0 or not prices: return 0
        N = len(prices)
        if k >= N:
            _sum = 0
            for i in range(1, N):
                if prices[i] > prices[i - 1]:
                    _sum += prices[i] - prices[i - 1]
            return _sum
        g = [0] * (k + 1)
        l = [0] * (k + 1)
        for i in range(N - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff)
                g[j] = max(l[j], g[j])
        return g[-1]
    