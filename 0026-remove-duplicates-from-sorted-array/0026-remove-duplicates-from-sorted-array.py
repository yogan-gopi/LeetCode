class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                nums[ind] = nums[i]
                ind += 1
        return ind
        
            