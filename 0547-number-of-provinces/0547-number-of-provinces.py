from collections import deque

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
                queue = deque([i])

                while queue:
                    curr = queue.popleft()
                    for neighbor in range(n):
                        if isConnected[curr][neighbor] == 1 and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

        return provinces