class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        suf = [0] * n

        pre[0] = nums[0]

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i]

        suf[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]

        res = [0] * n

        res[0] = suf[1]
        res[-1] = pre[-2]

        for i in range(1, n - 1):
            res[i] = pre[i - 1] * suf[i + 1]

        return res