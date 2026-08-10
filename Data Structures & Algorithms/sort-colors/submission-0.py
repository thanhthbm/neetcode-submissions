class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count: list[int] = [0] * 3
        for num in nums:
            count[num] += 1
        k = 0
        for i in range(0, 3):
            for j in range(0, count[i]):
                nums[k] = i
                k += 1

        
        