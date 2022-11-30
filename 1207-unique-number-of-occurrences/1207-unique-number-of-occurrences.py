class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set(arr)
        a = []
        for i in s:
            n = arr.count(i)
            if n in a:
                return False
            a.append(n)
        return True
        