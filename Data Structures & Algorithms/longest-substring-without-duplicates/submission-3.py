class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        last: dict[str, int] = {}
        left = 0
        ans = 0
        for i, c in enumerate(s):
            if c in last:
                left = max(left, last[c] + 1)
            last[c] = i
            ans = max(ans, i - left + 1)

        return ans
