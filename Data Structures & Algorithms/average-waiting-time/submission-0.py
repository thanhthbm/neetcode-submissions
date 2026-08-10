class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = customers[0][0] + customers[0][1]
        wait = [0] * len(customers)
        wait[0] = customers[0][1]
        for i in range(1, len(customers)):
            if customers[i][0] >= start:
                wait[i] = customers[i][1]
                start = customers[i][1] + customers[i][0]
            else:
                wait[i] = start - customers[i][0] + customers[i][1]
                start = customers[i][0] + wait[i]

        return sum(wait) / len(wait)