class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        seen: set[int] = set()

        for num in nums:
            if num in seen:
                dup = num
            else:
                seen.add(num)

        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)

        missing = expected - (actual - dup)

        return [dup, missing]