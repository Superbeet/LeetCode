"""OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """

        if not node:
            return None

        hashtable = {}
        stack = []
        stack.append(node)

        hashtable[node] = UndirectedGraphNode(node.label)

        while len(stack):
            p1 = stack.pop()
            p2 = hashtable[p1]

            for i in xrange(0, len(p1.neighbors)):
                nb = p1.neighbors[i]

                if nb in hashtable:
                    p2.neighbors.append(hashtable[nb])
                    
                else:
                    temp = UndirectedGraphNode(nb.label)
                    p2.neighbors.append(temp)
                    hashtable[nb] = temp
                    stack.append(nb)

        return hashtable[node]





        