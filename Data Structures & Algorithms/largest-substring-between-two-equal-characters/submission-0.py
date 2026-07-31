class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mp: dict[str, list[int]] = {}

        for i, c in enumerate(s):
            mp.setdefault(c, []).append(i)
            
        ans = -1
        for _, value in mp.items():
            if len(value) > 1:
                ans = max(ans, value[-1] - value[0] - 1)
        return ans