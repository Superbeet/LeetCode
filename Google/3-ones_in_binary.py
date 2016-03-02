m1 = 0x5555555555555555
m2 = 0x3333333333333333
m4 = 0x0f0f0f0f0f0f0f0f
m8 = 0x00ff00ff00ff00ff
m16= 0x0000ffff0000ffff
m32= 0x00000000ffffffff
hff= 0xffffffffffffffff

def bitCount(x):
	x = (x&m1) + ((x>>1)&m1)
	x = (x&m2) + ((x>>2)&m2)
	x = (x&m4) + ((x>>4)&m4)
	x = (x&m8) + ((x>>8)&m8)
	x = (x&m16) + ((x>>16)&m16)
	x = (x&m32) + ((x>>32)&m32)
	return x

num = 1025
print bitCount(num)