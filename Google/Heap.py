import heapq

class MinHeap(object):
	def __init__(self, k):
		self.k = k
		self.data = []
	
	def push(self, elem):
		if len(self.data)<self.k:
			heapq.heappush(self.data, elem)
		else:
			if elem > self.data[0]:
				heapq.heapreplace(self.data, elem)
	
	def pop(self):
		return heapq.heappop(self.data)
	
	def top_k(self):
		size = len(self.data)
		top_list = [heapq.heappop(self.data) for x in range(size)]
		return top_list[::-1]

class MaxHeap(object):
	def __init__(self, k):
		self.k = k
		self.data = []
	
	def push(self, elem):
		elem = -elem
		if len(self.data)<self.k:
			heapq.heappush(self.data, elem)
		else:
			if elem>self.data[0]:
				heapq.heapreplace(self.data, elem)
	
	def pop(self):
		return -heapq.heappop(self.data)
	
	def btm_k(self):
		size = len(self.data)
		top_list = [-heapq.heappop(self.data) for x in range(size)]
		return top_list[::-1]
	
if __name__ == "__main__":
	import random
	list_rand = random.sample(xrange(1000000), 100)
	th = MinHeap(10)
	for i in list_rand:
		th.push(i)
	print th.pop()
	print th.top_k()
	print sorted(list_rand, reverse=True)[0:10]
	
	list_rand = random.sample(xrange(1000000), 100)
	th = MaxHeap(10)
	for i in list_rand:
		th.push(i)
	print th.pop()
	print th.btm_k()
	print sorted(list_rand)[0:10]
	
	
	