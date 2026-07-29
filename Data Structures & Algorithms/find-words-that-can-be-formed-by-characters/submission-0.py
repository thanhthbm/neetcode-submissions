class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        base = [0] * 26

        for c in chars:
            base[ord(c) - ord('a')] += 1

        ans = 0

        for word in words:
            cnt = [0] * 26
            ok = True

            for c in word:
                idx = ord(c) - ord('a')
                cnt[idx] += 1
                if cnt[idx] > base[idx]:
                    ok = False
                    break

            if ok:
                ans += len(word)

        return ans