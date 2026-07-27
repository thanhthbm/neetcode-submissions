class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words.sort(key=len)
        res = []
        for i in range(len(words)):
            word = words[i]
            for j in range(i+1, len(words)):
                if word in words[j]:
                    res.append(word)
                    break

        return res