from collections import deque

class Solution:
    def orangesRotting(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        q = deque()
        fresh = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j, 0))   # (row, col, time)
                elif mat[i][j] == 1:
                    fresh += 1
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        
        # Step 2: BFS
        while q:
            r, c, t = q.popleft()
            time = max(time, t)  # track max time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    mat[nr][nc] = 2   # rot it
                    fresh -= 1
                    q.append((nr, nc, t + 1))
        
        # Step 3: If fresh still remains → impossible
        return -1 if fresh > 0 else time
