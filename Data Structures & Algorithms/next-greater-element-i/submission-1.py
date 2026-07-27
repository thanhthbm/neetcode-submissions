class Solution:
    def getNextGreaterList(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and (nums[i] > nums[stack[-1]]):
                idx = stack.pop()
                result[idx] = nums[i]
            stack.append(i)

        return result



    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map: dict[int, int] = {}
        for index, num in enumerate(nums2):
            map[num] = index

        next_greater_list = self.getNextGreaterList(nums2)

        result: list[int] = []
        for num in nums1:
            nums2_index = map.get(num)
            result.append(next_greater_list[nums2_index])

        return result


