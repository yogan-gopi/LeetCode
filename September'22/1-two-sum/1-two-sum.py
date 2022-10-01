class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i, j in enumerate(nums):
            if target - j in hash:
                return [hash[target-j], i]
            else:
                hash[j] = i
        return