# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        return True

    def peek(self):
        return self.stack[-1] 

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack)==0

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
    
        klist = []
        stk = stack()

        cur_node = root
        
        # inorder traversal
        while not stk.empty() or cur_node:
            
            while cur_node:
                stk.push(cur_node)
                cur_node = cur_node.left
        
            cur_node = stk.pop()

            # maintain a k-size list to track closet node values
            if len(klist) < k:
                klist.append(cur_node.val)

            else:
                first = klist[0]
                if abs(first-target)>abs(cur_node.val-target):
                    klist.pop(0)
                    klist.append(cur_node.val)
                else:
                    break
            # end

            cur_node = cur_node.right

        return klist

root = TreeNode(2)
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(1)

sol = Solution()
print sol.closestKValues(root, 0.000000, 5)