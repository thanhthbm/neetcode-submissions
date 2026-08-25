class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp: dict[str, int] = {}

        for index, c in enumerate(order):
            mp[c] = index

        return "".join(sorted(s, key=lambda x: mp.get(x, len(order))))