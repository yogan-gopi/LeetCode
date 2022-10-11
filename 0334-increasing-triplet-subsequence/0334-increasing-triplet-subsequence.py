class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        iMax, jMax = float(inf), float(inf)
        for i in nums:
            if i <= iMax:
                iMax = i
            elif i <= jMax:
                jMax = i
            else:
                return True
        return False
                    