class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans: list[int] = [0] * n

        for i in range(1, n):
            if boxes[i] == '1':
                ans[0] += i

        left = int(boxes[0])
        right = boxes.count('1') - left
        
        for i in range(1, n):
            ans[i] = ans[i - 1] + left - right

            if boxes[i] == '1':
                left += 1
                right -= 1

        return ans
