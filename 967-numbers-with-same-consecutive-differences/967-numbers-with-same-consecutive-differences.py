class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = []
        if N == 1:
            ans.append(0)

        def dfs(num, count):
            if count == N:
                res.append(int(num))
                return
            last_num = int(num[-1])
            if K == 0:
                dfs(num + str(last_num), count + 1)
                return
            for cur_num in [last_num + K, last_num - K]:
                if 0 <= cur_num <= 9:
                    dfs(num + str(cur_num), count + 1)

        for i in range(1, 10):
            dfs(str(i), 1)
        return res