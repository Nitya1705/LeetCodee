class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]


        if oldColor == color:
            return image

        queue = [(sr, sc)]
        image[sr][sc] = color

        while queue:
            r, c = queue.pop(0)

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == oldColor:
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image