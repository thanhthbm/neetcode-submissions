class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp: dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                if i - mp.get(nums[i], 0) <= k:
                    return True
            mp[nums[i]] = i

        return False