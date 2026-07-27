class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)

        max_odd = 0
        min_even = float("inf")

        for freq in cnt.values():
            if freq % 2:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even