class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: list[list[int]] = [[1]]
        for i in range(1, numRows):
            tmp: list[int] = [1]
            for j in range(1, i):
                tmp.append(result[i - 1][j - 1] + result[i - 1][j])
            tmp.append(1)
            result.append(tmp)

        return result

