class RateLimiter():
	def __init__(self, limit):
		self.queue = []
		self.limit = limit
		self.index = 0

	def check(self, data):
		cur_time = time.time()
		
		if cur_time - self.queue[self.index] <= limit:
			self.queue[self.index] = cur_time
			self.index += 1
			return True
		else:
			return False

import threading

class TokenBucket():
	def __init__(self, limit):
		self.bucket = []
		self.limit = limit
		timer = threading.Timer(1/limit, create_token)
		timer.start()

	def create_token(self):
		token = "x"
		if len(self.bucket) < self.limit:
			self.bucket.append()

	def check(self, data):
		if len(self.bucket) > 0:
			self.bucket.pop()
			return True
		else:
			return False

threadLock = threading.Lock()
threadLock.acquire()
threadLock.release()