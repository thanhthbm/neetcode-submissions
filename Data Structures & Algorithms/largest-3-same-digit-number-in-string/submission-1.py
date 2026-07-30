class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = -1
        for i in range(1, len(num) - 1):
            if num[i] == num[i - 1] == num[i + 1]:
                num_int = int(num[i - 1]) * 100 + int(num[i]) * 10 + int(num[i + 1])
                max_num = max(max_num, num_int)

        return str(max_num).zfill(3) if max_num != -1 else "" 

        