class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words: list[str] = s.split(" ")
        if len(pattern) != len(words):
            return False

        mp_pattern: dict[str, int] = {}
        mp_word: dict[str, int] = {}

        for idx, (c, word) in enumerate(zip(pattern, words)):
            if mp_pattern.get(c, -1) != mp_word.get(word, -1):
                return False
            mp_pattern[c] = idx
            mp_word[word] = idx

        return True