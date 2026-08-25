class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp: dict[int, int] = {}

        for x in arr1:
            mp[x] = mp.get(x, 0) + 1
        
        result: list[int] = []
        
        for x in arr2:
            result.extend([x] * mp.get(x, 0))
            mp.pop(x)

        for x in sorted(mp):
            result.extend([x] * mp.get(x, 0))

        return result

        

        
        
