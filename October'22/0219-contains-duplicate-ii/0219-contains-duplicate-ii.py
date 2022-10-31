class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i

        return False