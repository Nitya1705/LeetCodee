
from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        queue = deque()

        # Find the first land cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited.add((r, c))
                    break
            if queue:
                break

        perimeter = 0

        # BFS traversal
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    grid[nr][nc] == 0):
                    perimeter += 1

                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return perimeter
