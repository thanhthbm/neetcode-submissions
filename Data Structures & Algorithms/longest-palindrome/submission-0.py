class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp: dict[str, int] = {}

        for c in s:
            mp[c] = mp.get(c, 0) + 1
        
        ans = 0
        odd_count = 0
        
        for _, value in mp.items():
            if value % 2 == 0:
                ans += value
            else:
                odd_count += 1
                ans += value - 1

        if odd_count > 0:
            ans += 1
        return ans