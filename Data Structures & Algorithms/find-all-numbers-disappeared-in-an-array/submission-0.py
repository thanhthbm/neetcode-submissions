class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        se: set[int] = set()
        for x in nums:
            se.add(x)

        return [i for i in range(1, len(nums) + 1) if i not in se]