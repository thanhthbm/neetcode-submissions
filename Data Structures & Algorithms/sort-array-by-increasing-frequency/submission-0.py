class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp: dict[int, int] = {}
        for x in nums:
            mp[x] = mp.get(x, 0) + 1

        nums.sort(key = lambda x: (mp[x], -x))
        return nums