class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k = [0 for _ in range(101)]
        sorted_arr = []

        for height in heights:
            k[height] += 1

        # counting sort
        for i in range(101):
            if k[i] != 0:
                for j in range(k[i]):
                    sorted_arr.append(i)

        cnt = 0
        for i in range(len(heights)):
            if heights[i] != sorted_arr[i]:
                cnt += 1
        return cnt
