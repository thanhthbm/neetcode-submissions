class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfies = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfies += customers[i]
        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        ans = satisfies + extra

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                extra += customers[i]

            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            ans = max(ans, satisfies + extra)

        return ans

            
