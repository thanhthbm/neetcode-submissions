class Solution:
    def minOperations(self, s: str) -> int:
        diff0 = 0  # mẫu 010101...
        diff1 = 0  # mẫu 101010...

        for i, c in enumerate(s):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            if c != expected0:
                diff0 += 1
            if c != expected1:
                diff1 += 1

        return min(diff0, diff1)