class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = customers[0][0] + customers[0][1]
        total_wait = customers[0][1]

        for i in range(1, len(customers)):
            if customers[i][0] >= start:
                wait = customers[i][1]
                start = customers[i][0] + customers[i][1]
            else:
                wait = start - customers[i][0] + customers[i][1]
                start = customers[i][0] + wait

            total_wait += wait

        return total_wait / len(customers)