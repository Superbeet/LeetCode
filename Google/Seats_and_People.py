def add_people_num(seats):
	if not seats:
		return 0

	size = len(seats)
	count = 0
	start = -1
	end = 0
	while end<size:
		if seats[end]==1:
			if start == -1:
				count += (end-start-1)/2
			else:
				count += (end-start-2)/2
			start = end
		end += 1

	return count

print add_people_num([1,0,0,1])
print add_people_num([0,0,1,0,0,1])
print add_people_num([0,0,1,0,0,0,1])


