class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        ans = 0
        for i in range(k):
            window_sum += arr[i]

        if window_sum / k >= threshold:
            ans += 1
        
        for i in range(1, len(arr) - k + 1):
            window_sum -= arr[i - 1]
            window_sum += arr[i + k - 1]
            if window_sum / k >= threshold:
                ans += 1

        return ans