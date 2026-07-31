class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = [0] * 26

        for word in words:
            for c in word:
                cnt[ord(c) - ord('a')] += 1

        n = len(words)
        return all(x % n == 0 for x in cnt)