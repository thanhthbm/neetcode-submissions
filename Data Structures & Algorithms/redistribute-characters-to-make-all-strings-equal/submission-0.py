class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp: dict[str, int] = {}
        for word in words:
            for c in word:
                mp[c] = mp.get(c, 0) + 1
        
        for _, value in mp.items():
            n = len(words)
            if not value % n == 0:
                return False

        return True