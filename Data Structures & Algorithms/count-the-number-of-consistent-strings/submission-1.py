class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        cnt = 0
        for word in words:
            word_set = set(word)
            if word_set.issubset(allowed_set):
                cnt += 1

        return cnt
