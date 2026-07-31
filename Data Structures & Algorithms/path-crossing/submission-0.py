class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mp: dict[str, tuple[int, int]] = {
            "N": (0, -1),
            "S": (0, 1),
            "W": (-1, 0),
            "E": (1, 0)
        }

        visited: set[tuple[int, int]] = set()
        visited.add((0, 0))

        x = 0
        y = 0

        for c in path:
            new_x = mp[c][0] + x
            new_y = mp[c][1] + y
            if (new_x, new_y) in visited:
                return True

            visited.add((new_x, new_y))
            x = new_x
            y = new_y
        
        return False
