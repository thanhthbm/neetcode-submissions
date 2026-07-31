class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        mp = Counter(students)

        for sandwich in sandwiches:
            if mp[sandwich] == 0:
                break
            mp[sandwich] -= 1

        return mp[0] + mp[1]