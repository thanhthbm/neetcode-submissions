class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp: dict[int, int] = {}

        for x in nums:
            mp[x] = mp.get(x, 0) + 1

        cnt = 0
        for _, value in mp.items():
            cnt += value * (value - 1) // 2

        return cnt