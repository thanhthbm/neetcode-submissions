class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = nums[0] < nums[-1]

        for i in range(1, len(nums)):
            if increasing:
                if nums[i] < nums[i - 1]:
                    return False
            else:
                if nums[i] > nums[i - 1]:
                    return False

        return True