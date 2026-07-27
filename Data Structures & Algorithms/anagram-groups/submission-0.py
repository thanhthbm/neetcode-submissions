class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map: dict[tuple[int], list[str]]= {}
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            map.setdefault(tuple(key), []).append(word)
        return [value for _, value in map.items()]