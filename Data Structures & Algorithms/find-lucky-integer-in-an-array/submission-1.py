class Solution:
    def findLucky(self, arr: List[int]) -> int:
        k = [0 for _ in range(501)]
        for x in arr:
            k[x] += 1

        for i in range(500, 0, -1):
            if i == k[i]:
                return i
        return -1