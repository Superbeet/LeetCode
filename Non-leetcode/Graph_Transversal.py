class Node:
    def __init__(self, value):
      self.value = value
      self.adjacentNodes = []

# DFS recusion - stack
def DFS(node, soughtValue, visitedNodes):
    if node.value == soughtValue:
        return True

    visitedNodes.add(node)

    for adjNode in node.adjacentNodes:
        if adjNode not in visitedNodes:
            if DFS(adjNode, soughtValue, visitedNodes):
                return True

    return False

# DFS iteration
def DFS(node, soughtValue, visistedNodes):
    visitedNodes = set()

    stack = []
 
    while len(stack) > 0:
        node = stack.pop(-1)
        if node in visitedNodes:
            continue

        visitedNodes.add(node)

        if node.value == soughtValue:
            return True

        for n in node.adjacentNodes:
            if n not in visitedNodes:
                stack.append(n)

    return False    

# BFS iteration
def BFS(node, soughtValue):

    visitedNodes = set()

    queue = []
 
    while len(queue) > 0:
        node = queue.pop(0)
        if node in visitedNodes:
            continue

        visitedNodes.add(node)

        if node.value == soughtValue:
            return True

        for n in node.adjacentNodes:
            if n not in visitedNodes:
                queue.append(n)

    return False

# BFS recurstion, not good idea, call stack is a stack
