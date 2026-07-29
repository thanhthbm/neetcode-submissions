class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp: dict[str, int] = {}
        for c in magazine:
            mp[c] = mp.get(c, 0) + 1
        for c in ransomNote:
            if c not in mp:
                return False
            mp[c] -= 1
            if mp[c] < 0:
                return False

        return True