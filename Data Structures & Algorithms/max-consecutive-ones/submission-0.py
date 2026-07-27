class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 1 if nums[0] == 1 else 0
        cnt = max_len

        for i in range(1, len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:            
                cnt = 0
            max_len = max(max_len, cnt)

        return max_len
