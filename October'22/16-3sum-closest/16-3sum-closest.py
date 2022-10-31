class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort() # sort
        result = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            left, right = i + 1, n-1
            while left <right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target: return sum
                if abs(sum-target) <abs(result-target): result = sum #Update the optimal value

                if sum <target: left += 1 # move to the right
                elif sum> target: right -= 1 # Move to the left

        return result