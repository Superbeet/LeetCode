"""
Inorder list to put nodes with order. Keep a descending stack.
If element is smaller than last node of inorder list, return False.
O(n) time, O(n) stack
"""
# class Solution(object):
#     def verifyPreorder(self, preorder):
#         """
#         :type preorder: List[int]
#         :rtype: bool
#         """
#         inorder = []
#         stack = []

#         for p in preorder:
            
#             if inorder and p<inorder[-1]:
#                 return False

#             while stack and p>stack[-1]:
#                 inorder.append(stack.pop())

#             stack.append(p)

#             print "stack  ->[%s]" %(stack)
#             print "inorder->[%s]" %(inorder)

#         return True
"""
Next, we can replace inorder list with a variable low. 
low is equal as last element of inorder list in Solution 1.
O(n) time, O(n) stack
"""
# class Solution(object):
#     def verifyPreorder(self, preorder):
#         """
#         :type preorder: List[int]
#         :rtype: bool
#         """
#         low = -1
#         stack = []

#            for num in preorder:
#                if num<low:
#                    return False

#                while stack and num>stack[-1]:
#                    low = stack.pop()

#                stack.append(num)

#            return True

"""
In-order replace element of preorder list as stack in Solution 2. 
i is at last element of stack. 
O(n) time, O(1) space
"""
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = -1
        i = -1

        for num in preorder:
            if num<low:
                return False

            while i>=0 and num>preorder[i]:
                low = preorder[i]
                i -= 1

            i += 1
            preorder[i]=num

        return True



# root = TreeLinkNode(6)
# root.left = TreeLinkNode(3)
# root.left.left = TreeLinkNode(1)
# root.left.right = TreeLinkNode(4)
# root.right = TreeLinkNode(8)
# root.right.right = TreeLinkNode(10)
# root.right.right.right = TreeLinkNode(12)

preorder = [6,3,1,4,8,10]

sol = Solution()
sol.verifyPreorder(preorder)