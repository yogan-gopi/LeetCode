class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def checkTri(a, b, c):
            if (a + b <= c) or (a + c <= b) or (b + c <= a) :
                return False
            else:
                return True     

        
        nums.sort()
        n = len(nums)
        for i in range(n-1, 1, -1):
            l3 = nums[i]
            l2 = nums[i-2]
            l1 = nums[i-1]
            
            if l3 < (l1+l2):
                return (l1+l2+l3)
        return 0
            

        
            