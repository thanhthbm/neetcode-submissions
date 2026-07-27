class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        last_s: dict[str, int] = {}
        last_t: dict[str, int] = {}

        for i in range(len(s)):
            if last_s.get(s[i], -1) != last_t.get(t[i], -1):
                return False

            last_s[s[i]] = i
            last_t[t[i]] = i

        return True