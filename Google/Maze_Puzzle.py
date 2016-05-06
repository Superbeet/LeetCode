import copy
class Maze(object):
    def solve_maze_util(self, maze, start, terminal):
        h = len(maze)
        if h == 0:
            return []
            
        w = len(maze[0])
        
        self.terminal = terminal
        
        self.res = []
        visited = [[False for i in range(w)] for j in range(h)]
        self.dfs(maze, h, w, start[0], start[1], visited, [(0,0)])
        return self.res
    
    def is_valid(self, maze, h, w, y, x):
        if 0<=y<h and 0<=x<w and maze[y][x]==1:
            return True
        else:
            return False
        
    def dfs(self, maze, height, width, y, x, visited, sol):            
        if x == self.terminal[0] and y == self.terminal[1]:
            self.res.append(sol)
            return True
            
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for dy,dx in dirs:
            ny = y+dy
            nx = x+dx
            
            if self.is_valid(maze, height, width, ny, nx) and not visited[ny][nx]:                
                sol.append((nx, ny))
                visited[ny][nx] = True
                if self.dfs(maze, height, width, ny, nx, 
                    copy.deepcopy(visited), copy.deepcopy(sol)):
                    return True
                visited[ny][nx] = False
                sol.pop(-1)
            
        return False

        
matrix = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0],
]

maze = Maze()
print maze.solve_maze_util(matrix, (0,0), (0,4))
    
    
            