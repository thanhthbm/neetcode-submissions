class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for num in nums:
            count[min(n, num)] += 1

        greater_or_equal = 0
        for x in range(n, 0, -1):
            greater_or_equal += count[x]
            if x == greater_or_equal:
                return x

        return -1