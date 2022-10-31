class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        for i in range(n-1, 1, -1):
            l3 = nums[i]
            l2 = nums[i-2]
            l1 = nums[i-1]
            
            if l3 < (l1+l2):
                return (l1+l2+l3)
        return 0
            

        
            