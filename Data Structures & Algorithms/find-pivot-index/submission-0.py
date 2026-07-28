class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0] * len(nums)
        pre[0] = nums[0]

        for i in range(1, len(nums)):
            pre[i] = nums[i] + pre[i - 1]

        for i in range(len(nums)):
            left_sum = pre[i - 1] if i > 0 else 0
            right_sum = pre[-1] - left_sum - nums[i]
            if left_sum == right_sum:
                return i

        return -1