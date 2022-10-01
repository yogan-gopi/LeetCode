class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        maxi = 0
        dp =[[0 for _ in range(n2+1)] for _ in range(n1+1)]
        
        for i in range(1, n1+1):
            
            for j in range(1, n2+1):
                
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = (dp[i-1][j-1] + 1)
                    maxi = max(maxi, dp[i][j])
                    
        return maxi
            