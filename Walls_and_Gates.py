# Without pruning
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        h = len(rooms)
        if h==0:
            rooms = []
        else:
            w = len(rooms[0])

            for y in xrange(0, h):
                for x in xrange(0, w):
                    if rooms[y][x]==0:
                        self.doBFS(rooms, h, w, y, x)

    def doBFS(self, matrix, height, width, y, x):
        # visited_pos[y][x] = 0

        queue = []
        queue.append([y,x])
        count = 0
        visited = {}
        visited[(y,x)] = True

        while len(queue):
            size = len(queue)

            for k in xrange(0, size):
                y,x = queue.pop(0)
                matrix[y][x] = min(matrix[y][x], count)

                dirs = [(-1,0),(1,0),(0,-1),(0,1)]
                for dy,dx in dirs:
                    ny = y+dy
                    nx = x+dx
                    # print "[%s,%s] %s %s" %(ny, nx, matrix[ny][nx], ((y,x) not in visited))
                    if (0<=ny<height and 0<=nx<width) and matrix[ny][nx]!=-1 and matrix[ny][nx]>0 and ((ny,nx) not in visited):
                        # print matrix[ny][nx]
                        # print "------"
                        queue.append((ny,nx))
                        visited[(ny,nx)] = True
            count += 1

sol = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

print "-- Before --\n"
printf(rooms)
print "-- After --\n" %rooms
printf(sol.wallsAndGates(rooms))