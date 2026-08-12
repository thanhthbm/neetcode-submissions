class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(len(nums)):
            if nums[k - 1] != nums[i]:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

        return k