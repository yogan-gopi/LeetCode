class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        vis = []
        res = []
        for i in nums:
            if nums.count(i) == 2:
                res.append(i)
                break
        for i in range(len(nums)):
            if i+1 not in nums:
                res.append(i+1)
                break
            
        return res