class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp: dict[str, int] = {}
        for c in magazine:
            mp[c] = mp.get(c, 0) + 1
        for c in ransomNote:
            if mp.get(c, 0) == 0:
                return False
            mp[c] -= 1

        return True