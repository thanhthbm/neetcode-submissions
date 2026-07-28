class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mp: dict[int, int] = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in mp:
                    mp[grid[i][j]] = 1
                else:
                    mp[grid[i][j]] += 1

        res: list[int] = []
        n = len(grid)
        for i in range(1, n * n + 1):
            if i not in mp:
                res.append(i)
            elif mp[i] == 2:
                res.append(i)

        if res[0] not in mp:
            res[0], res[1] = res[1], res[0]

        return res