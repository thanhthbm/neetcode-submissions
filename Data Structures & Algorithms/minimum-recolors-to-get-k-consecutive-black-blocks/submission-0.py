class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0

        for i in range(k):
            if blocks[i] == 'W':
                white += 1

        min_white = white

        for i in range(1, len(blocks) - k + 1):
            current_white = white

            if blocks[i - 1] == 'W':
                current_white -= 1

            if blocks[i + k - 1] == 'W':
                current_white += 1

            min_white = min(min_white, current_white)
            white = current_white

        return min_white