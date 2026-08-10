class Solution:
    def vowelStrings(
        self,
        words: List[str],
        queries: List[List[int]]
    ) -> List[int]:
        n = len(words)
        vowels = "ueoai"

        pre: list[int] = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = pre[i] + (
                words[i][0] in vowels and words[i][-1] in vowels
            )

        res: list[int] = []

        for query in queries:
            res.append(
                pre[query[1] + 1] - pre[query[0]]
            )

        return res