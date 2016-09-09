"""
LinkedIn: Can I Win
http://blog.csdn.net/craiglin1992/article/details/44929861
    In "the 100 game," two players take turns adding, to a running 
    total, any integer from 1..10. The player who first causes the running 
    total to reach or exceed 100 wins. 
    What if we change the game so that players cannot re-use integers? 
    For example, if two players might take turns drawing from a common pool of numbers 
    of 1..15 without replacement until they reach a total >= 100. This problem is 
    to write a program that determines which player would win with ideal play. 

    Write a procedure, "Boolean canIWin(int maxChoosableInteger, int desiredTotal)", 
    which returns true if the first player to move can force a win with optimal play. 

    Your priority should be programmer efficiency; don't focus on minimizing 
    either space or time complexity. 
"""

def Solution():
	def __init__(self, max_choosable_integer, desired_total):
		if max_choosable_integer<=0 or desired_total<=0:
			return False

		
		pool = []
		for i in xrange(1, max_choosable_integer+1):
			pool.add(i)

		used = [False for i in xrange(max_choosable_integer)]

	def can_win(self, pool, used, targeted_total):

		size = len(pool)

		for j in xrange(size-1, -1, -1):
			if visited[j]:
				continue
				
			if pool[j] >= targeted_total:
				return True

		for i in xrange(size):
			if visited[i]:
				continue

			visited[i] = True

			if not self.can_win(pool, used, targeted_total-pool[i]):
				return True

			visited[i] = False

		return False


