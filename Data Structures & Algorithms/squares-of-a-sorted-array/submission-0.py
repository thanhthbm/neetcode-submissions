class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        cur = len(nums) - 1
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        while l <= r:
            if nums[l] < nums[r]:
                res[cur] = nums[r]
                r -= 1
            else:
                res[cur] = nums[l]
                l += 1
            cur -= 1
        
        return res
