class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for i in strs:
            count = [0 for _ in range(26)]
            for j in i:
                count[ord(j)-ord("a")] += 1
                
            res[tuple(count)].append(i)
        return res.values()