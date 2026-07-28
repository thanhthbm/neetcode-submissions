class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # b: 1, a: 1, l: 2, o: 2, n: 1
        mp: dict[str, int] = {}

        for c in text:
            mp[c] = mp.get(c, 0) + 1

        return min(
            mp.get("a", 0), mp.get("b", 0), mp.get("l", 0) // 2, mp.get("o", 0) // 2, mp.get("n", 0)
        )
