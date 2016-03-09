import time
import threading 

class TTLHashMap(object):
	def __init__(self):
		self.hash_map = {}
		self.lock = threading.Lock()
		
	def __counter__(self):
		pass
		
	def put(self, key, value, ttl):
		entry_time = time.time()
		self.hash_map[key] = [value, ttl, entry_time]	
		
	def get(self, key):
		slot = self.hash_map[key]
		value, ttl, entry_time = slot[0], slot[1], slot[2]
		cur = time.time()
		
		self.lock.acquire()
		
		if entry_time + ttl < cur:
			del self.hash_map[key]
			self.lock.release()
			return False
		else:
			self.hash_map[key][2] = cur
			self.lock.release()
			return value

		# def stop(self):
		# self.timer.cancel()
	
if __name__ == '__main__':
	hash_map = TTLHashMap()
	hash_map.put(0, 0, 0)
	hash_map.put(4, 4, 4)
	time.sleep(3)
	print hash_map.get(0)
	print hash_map.get(4)