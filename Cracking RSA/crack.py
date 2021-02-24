import sys
import random
import math
import time
import matplotlib.pyplot as plt

def modular_pow(base, exponent, modulus):
	res = 1
	while (exponent>0):
		if (exponent & 1):
			res = (res*base)%modulus
		exponent = exponent >> 1
		base = (base*base)%modulus
	return res

def pollard_rho(n):
	if n == 1:
		return n
	if (n%2 == 0):
		return 2
	x = 8
	y = x
	c = 3
	d = 1
	while (d == 1):
		x = (modular_pow(x, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		d = math.gcd(abs(x - y), n)
	return d
def factors(num):
	f1 = pollard_rho(num)
	f2 = int(num//f1)
	return (f1,f2)

def main():
	num = int(sys.argv[1])

	# pl_txt_name = sys.argv[2]
	# string = (open(sys.argv[1]).read().strip())
	# num_list_str = string.split('\n')
	# num_list = [int(x) for x in num_list_str]

	# num_sizes = []
	# fac_times = []
	# count = 1
	# for num in num_list:
	# 	start = time.time()
	# 	(f1,f2) = factors(num)
	# 	end = time.time()
	# 	num_sizes.append(len(str(num)))
	# 	fac_times.append(end-start)
	# 	print (count, f1, f2)
	# 	count += 1
	# 	print ("Time taken =", (end - start))
	# write_file = open("out.txt", "w")
	# write_file.write(str(num_sizes))
	# write_file.write("\n")
	# write_file.write(str(fac_times))
	# plt.figure()
	# plt.xlabel("Number of Digits")
	# plt.ylabel("Time taken to factorise")
	# plt.scatter(num_sizes, fac_times)
	# plt.savefig("plot1_poll.png", dpi = 200)
	# plt.show()
	start = time.time()
	(p,q) = factors(num)
	end = time.time()
	t = (end - start)
	phi = (p-1)*(q-1)
	print ("p =",p)
	print ("q =",q)
	print ("t =",t)
	# print (phi)
	e = 1
	temp_count = 1
	for i in range(3,phi):
		if (math.gcd(i,phi) == 1):
			e = i
			temp_count += 1
		if temp_count > 5 :
			break
	print ("e =", e)
	k = 1
	while True:
		# print (k)
		if (pow((1 + k*phi),1,e) == 0) :
			d = int((1 + k*phi)//e)
			break
		k += 1
	print ("d =", d)
	# print ((d*e)%phi)

	plaintext = open(sys.argv[2]).read()
	M = [];
	for ch in plaintext.strip():
		M.append(ord(ch))
	C = []
	for val in M:
		en_val = (val**e)%num
		C.append(en_val)
	# print (M)
	print ("C =",C)
	D = []
	for val in C:
		D.append(pow(val, d, num))
	print ("M =",D)
	decrypt_plt = ""
	for i in D:
		decrypt_plt += chr(i)
	# print (decrypt_plt)
if __name__ == "__main__":
	main()