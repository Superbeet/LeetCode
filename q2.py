# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain 
# a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node1 = l1
        node2 = l2

        carry = 0
        last_node = None

        while node1 is not None or node2 is not None or carry != 0:

        	if node1 is not None:
        		value1 = node1.val
        	else:
        		value1 = 0

        	if node2 is not None:
        		value2 = node2.val
        	else:
        		value2 = 0

        	integer = (value1+value2+carry) % 10
        	carry = (value1+value2+carry) / 10
        	
        	# print "integer->%d, carry->%d" %(integer, carry)

        	new_node = ListNode(integer)

        	if last_node is not None:
        		last_node.next = new_node
        	else:
        		first_node = new_node

        	last_node = new_node

        	if node1 is not None:
        		node1 = node1.next
        	else:
        		node1 = None

        	if node2 is not None:
        		node2 = node2.next
        	else:
        		node2 = None


        return first_node

def createLinkedList(value_list):

	last_node = None

	for i in value_list:

		new_node = ListNode(i)

		if last_node is not None:

			last_node.next = new_node

		else:

			first_node = new_node

		last_node = new_node

	return first_node

if __name__ == '__main__':
	sol = Solution()
	list1 = [1]
	list2 = [9, 9]

	l1 = createLinkedList(list1)
	l2 = createLinkedList(list2) 
	
 	# first_node = sol.addTwoNumbers(l1, l2)

	node = sol.addTwoNumbers(l1, l2)

	result = "Lowest Digit"

	while node is not None:

		result = result + "->" + str(node.val)

		node = node.next 

	print result




