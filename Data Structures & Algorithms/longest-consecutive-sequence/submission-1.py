class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        se: set[int] = set(nums)

        max_len = 1

        for x in se:
            if x - 1 in se:
                continue
            cur_len = 1
            current = x
            while current + 1 in se:
                current += 1
                cur_len += 1
            max_len = max(max_len, cur_len)

        return max_len
