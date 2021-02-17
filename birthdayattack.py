import sys
import hashlib
import random
import string

def main():
	l_d = int(sys.argv[1])

	
	s1 = ""
	s2 = ""
	N = random.randint(1,20)
	
	for i in range(3):
		storage = {}
		dummy_storage = {}
		n = 0
		m = 0
		while True:
			n += 1
			res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
			m += sys.getsizeof(res)
			strin = res.encode()
			# print (res)
			hex_d = str(hashlib.sha3_256(strin).hexdigest())[:6]
			# print (hex_d)
			binary = "{0:08b}".format(int(hex_d, 16))
			binary = binary[:l_d]
			# print (binary)
			if binary not in storage.keys():
				h__h = str(hashlib.sha3_256(strin).hexdigest())
				hh = "{0:08b}".format(int(h__h, 16))
				dummy_storage[res] = hh
				storage[binary] = res
			else:
				s1 = storage[binary]
				s2 = res
				h_ = str(hashlib.sha3_256(strin).hexdigest())
				h2 = "{0:08b}".format(int(h_, 16))
				h1 = dummy_storage[s1]
				break

		print("s1 =", s1)
		print("s2 =", s2)
		print("h1 =",h1)
		print("h2 =",h2)
		print("m =",m)
		print("n =",n)
if __name__ == "__main__":
	main()