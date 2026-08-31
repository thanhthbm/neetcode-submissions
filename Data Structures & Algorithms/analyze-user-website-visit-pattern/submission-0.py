class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict
        from itertools import combinations

        users = defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            users[u].append((t, w))
        
        score = defaultdict(int)

        for visits in users.values():
            visits.sort()
            websites = [w for _, w in visits]
            patterns = set(combinations(websites, 3))
            for pattern in patterns:
                score[pattern] += 1
        
        return list(min(score, key = lambda x: (-score[x], x)))