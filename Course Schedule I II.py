class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        
        indegrees  = [0 for i in xrange(numCourses)]
        graph = {}
        
        for cur, prev in prerequisites:
            if pre not in graph:
                graph[pre] = [cur]
            else:
                graph[pre].append(cur)
            indegrees[cur] += 1
        
        from collections import deque
        queue = deque([])

        for i in xrange(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        count = 0
        # result = [-1 for i in xrange(numCourses)]

        while queue:
            cur = queue.popleft()
            # result[count] = cur
            count += 1
            if cur in graph:
                for nb in graph[cur]:
                    indegrees[nb] -= 1
                    if indegrees[nb] == 0:
                        queue.append(nb)
        
        if count == numCourses:
            return True
        
        else:
            return False

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        indegrees  = [0 for i in xrange(numCourses)]
        graph = {}
        
        for cur, pre in prerequisites:
            if pre not in graph:
                graph[pre] = [cur]
            else:
                graph[pre].append(cur)
            indegrees[cur] += 1
        
        from collections import deque
        queue = deque([])

        for i in xrange(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        count = 0
        
        result = [-1 for i in xrange(numCourses)]

        while queue:
            cur = queue.popleft()
            result[count] = cur
            count += 1
            if cur in graph:
                for nb in graph[cur]:
                    indegrees[nb] -= 1
                    if indegrees[nb] == 0:
                        queue.append(nb)
        
        if count == numCourses:
            return result
        
        else:
            return []



                  

                  
         
        
        
        
        