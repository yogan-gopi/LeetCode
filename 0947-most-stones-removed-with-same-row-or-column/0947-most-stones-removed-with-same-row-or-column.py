class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.parents = {}
        self.count = 0

        def find(x):
            if x not in self.parents:
                self.parents[x] = x
                self.count += 1
            if self.parents[x] != x:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                self.parents[rooty] = rootx
                self.count -= 1

        for x, y in stones:
            union(x + 10001, y)

        return len(stones) - self.count