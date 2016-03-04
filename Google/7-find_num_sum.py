# memorialization
def find_number_sum(num_array, value):
	size = len(num_array)
	memo = [[False for i in range(size)] for j in range(size)]
	
	def array_to_num(num_array):
		size = len(num_array)
		num = 0
		for i in xrange(0, size):
			num += num_array[i]*(10**(size-1-i))
		return num

	def cal_number_sum(num_array, i, val, cur_sum):
		if i==len(num_array) and cur_sum==val:
			return True
		
		for j in xrange(i, len(num_array)):
			if memo[i][j] != False:
				cur_sum += memo[i][j]
			else:
				temp = array_to_num(num_array[i:j+1])
				memo[i][j] = temp
				cur_sum += temp
			return cal_number_sum(num_array, j+1, val, cur_sum)
			
		return False
	
	return cal_number_sum(num_array, 0, value, 0)

# bruteforce
def find_number_sum_2(num_array, value):

	def array_to_num(num_array):
		size = len(num_array)
		num = 0
		for i in xrange(0, size):
			num += num_array[i]*(10**(size-1-i))
		return num

	def cal_number_sum(num_array, val, cur_sum):
		if not num_array and cur_sum==val:
			return True
		
		for i in xrange(0, len(num_array)):
			cur_sum += array_to_num(num_array[0:i+1])
			return cal_number_sum(num_array[i+1:], val, cur_sum)
			
		return False

	return cal_number_sum(num_array, value, 0)

import timeit
# array = [1,5,0,2,3,0,1,5,4,0,6,8,0,0,0,1]*10
array = [1,5,0,0,0,0,0,0,0,0,2]*10
timer_start = timeit.default_timer()
print find_number_sum(array, 80)
timer_1 = timeit.default_timer()
print find_number_sum_2(array, 80)
timer_2 = timeit.default_timer()

print "memo solution -> %s" %(timer_1-timer_start)
print "bruteforce solution -> %s" %(timer_2-timer_1)


# array_to_num([0])