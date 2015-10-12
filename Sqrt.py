class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		i = 0
		j = (x/2+1)/2
		pilot = None

		while i <= j:

			pilot = (i+j)/2

			if pilot^2 == x:
				return pilot

			if pilot^2 < x:
				i = pilot+1

			if pilot^2 > x:
				j = pilot-1

		return pilot

class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		i = 0
		j = 1
		pilot = 0

		while int(j) != int(i):
			i = j
			j = 1.0/2.0 * (i + x/i)

		return int(i)




sol = Solution()
print sol.mySqrt(0)