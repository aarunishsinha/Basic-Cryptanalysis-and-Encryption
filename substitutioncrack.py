import sys
import heapq
import string

class PriorityQueue:
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)
def freqs(cipher_t):
	letter_freqs = {"a":8.12, "b":1.49, "c":2.71, "d":4.32, "e":12.00, "f":2.30, "g":2.03,
    "h":5.92, "i":7.31, "j":0.10, "k":0.69, "l":3.98, "m":2.61, "n":6.95, "o":7.68,
    "p":1.82, "q":0.11, "r":6.02, "s":6.28, "t":9.10, "u":2.88, "v":1.11, "w":2.09,
    "x":0.17, "y":2.11, "z":0.07}
	charset_sub = {}
	aplhabet_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	sub_map_array = ['1','2','3','4','5','6','7','8','9','0','@','#','$','z','y','x','w','v','u','t','s','r','q','p','o','n']
	for ch in sub_map_array:
		charset_sub[ch] = 0
	
	ciph = cipher_t.replace(" ", "")
	ciph = ciph.replace(",", "")
	ciph = ciph.replace(".","")
	for ch in ciph:
		if ch in charset_sub:
			charset_sub[ch] += 1
	for ch in sub_map_array:
		charset_sub[ch] /= len(ciph)
		charset_sub[ch] *= 100
	# print (charset_sub)

	english = PriorityQueue()
	sub_map = PriorityQueue()

	for ch in aplhabet_array:
		english.push(ch, letter_freqs[ch])
	for ch in sub_map_array:
		sub_map.push(ch, charset_sub[ch])

	english_freq = []
	charset_freq = []
	while not english.isEmpty():
		ch1 = english.pop()
		ch2 = sub_map.pop()
		english_freq.append(ch1)
		charset_freq.append(ch2)

	english_freq = list(reversed(english_freq))
	charset_freq = list(reversed(charset_freq))
	return english_freq,charset_freq

def digraphs_and_trigraphs(cipher_t):
	text = cipher_t.replace(".", "")
	text = text.replace(",", "")
	tokens = text.split()
	digra = {}
	trigra = {}
	for word in tokens:
		if len(word) == 2:
			if word in digra.keys():
				digra[word] += 1
			else:
				digra[word] = 1
		elif len(word) == 3:
			if word in trigra.keys():
				trigra[word] += 1
			else:
				trigra[word] = 1
	return digra,trigra
#{'9': 'e', 'o': 't', '$': 'a', 'v': 'o', '2': 'i', 'y': 'n',
# '@': 's', '5': 'r', 'q': 'h', '0': 'd', '8': 'l', 't': 'u',
# 's': 'c', 'u': 'm', '3': 'f', '#': 'y', 'p': 'w', '7': 'g',
# 'x': 'p', '1': 'b', 'w': 'v', '6': 'k', 'r': 'x', '4': 'q',
# 'n': 'j', 'z': 'z'}
def cipher1(filename):
	file = open(filename)
	cipher_t = file.read().strip()
	plain_t = cipher_t.replace("v", "A")
	plain_t = plain_t.replace("9", "E")
	plain_t = plain_t.replace("o", "T")
	plain_t = plain_t.replace("q", "H")
	plain_t = plain_t.replace("5", "I")
	plain_t = plain_t.replace("y", "S")
	plain_t = plain_t.replace("$", "O")
	plain_t = plain_t.replace("#", "W")
	plain_t = plain_t.replace("2", "R")
	plain_t = plain_t.replace("@", "N")
	plain_t = plain_t.replace("8", "D")
	plain_t = plain_t.replace("u", "L")
	plain_t = plain_t.replace("6", "V")
	plain_t = plain_t.replace("7", "G")
	plain_t = plain_t.replace("p", "F")
	plain_t = plain_t.replace("t", "C")
	plain_t = plain_t.replace("0", "M")
	plain_t = plain_t.replace("3", "P")
	plain_t = plain_t.replace("1", "B")
	plain_t = plain_t.replace("s", "U")
	plain_t = plain_t.replace("4", "Q")
	plain_t = plain_t.replace("x", "Y")
	plain_t = plain_t.replace("w", "K")
	plain_t = plain_t.replace("r", "X")
	plain_t = plain_t.replace("z", "Z")
	
	
	return (plain_t.lower())


#{'q': 'e', 'y': 't', 'n': 'a', 'v': 'o', '@': 'i', 'r': 'n',
# '1': 's', 't': 'r', '$': 'h', 'p': 'd', '4': 'l', 'z': 'u',
# '#': 'c', '5': 'm', '3': 'f', '7': 'y', 'w': 'w', '9': 'g',
# 's': 'p', '8': 'b', '2': 'v', 'x': 'k', '6': 'x', 'o': 'q',
# 'u': 'j', '0': 'z'}

#{'nq': 9, '@$': 2, 'y$': 1, '$t': 1, 'r@': 1}

#{'1yz': 1, 'nrv': 3, '7qz': 1, 'zrz': 1, 'y$@': 2, '51v': 6,
# '144': 2, '@nq': 1, '7#@': 2, 'vqq': 1, 'w$t': 1}
def cipher2(filename):
	file = open(filename)
	cipher_t = file.read().strip()
	digra,trigra = digraphs_and_trigraphs(cipher_t)
	# print (digra)
	# print (trigra)
	plain_t = cipher_t.replace("q", "E")
	plain_t = plain_t.replace("4", "L")
	plain_t = plain_t.replace("1", "A")
	plain_t = plain_t.replace("n", "H")
	plain_t = plain_t.replace("9", "V") #Leaving
	plain_t = plain_t.replace("r", "I")
	plain_t = plain_t.replace("y", "N")
	plain_t = plain_t.replace("p", "G")
	plain_t = plain_t.replace("z", "D") #zrz
	plain_t = plain_t.replace("t", "R") #Dinner
	plain_t = plain_t.replace("$", "O") #N$ -> NO
	plain_t = plain_t.replace("@", "T") #NO@ -> NOT
	plain_t = plain_t.replace("v", "S") #HIv -> HIS
	plain_t = plain_t.replace("7", "B") #7ED -> BED
	plain_t = plain_t.replace("5", "W") #5ENT -> WENT
	plain_t = plain_t.replace("#", "U") ##NIVERSE -> UNIVERSE
	plain_t = plain_t.replace("8", "P") #SLEE8 -> SLEEP
	plain_t = plain_t.replace("3", "C")
	plain_t = plain_t.replace("s", "M")
	plain_t = plain_t.replace("w", "F")
	plain_t = plain_t.replace("2", "Y")
	plain_t = plain_t.replace("6", "K")
	plain_t = plain_t.replace("x", "J")
	plain_t = plain_t.replace("0", "Z")
	plain_t = plain_t.replace("u", "Q")
	plain_t = plain_t.replace("o", "X")
	return plain_t.lower()
def main():
	filename = sys.argv[1]
	if filename == "cipher1.txt":
		plain_t = cipher1(filename)
	else:
		plain_t = cipher2(filename)
	print (plain_t)
if __name__ == "__main__":
	main()