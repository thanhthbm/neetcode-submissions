class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfy = 0
        for (customer, grump) in zip(customers, grumpy):
            if grump == 0:
                satisfy += customer

        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        ans = satisfy + extra
        for i in range(1, len(grumpy) - minutes + 1):
            if grumpy[i - 1] == 1:
                extra -= customers[i - 1]
            if grumpy[i + minutes - 1]:
                extra += customers[i + minutes - 1]

            ans = max(ans, satisfy + extra)
        return ans
