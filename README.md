# Basic-Cryptanalysis-and-Encryption
SIL765 - Network and System Security\
Basic Cryptanalysis, Birthday Attack and Cracking RSA

## Basic Cryptanalysis 
### To-Do:
- Utilise a basic cryptanalysis technique to break a monoalphabetic cipher.

Character Set for substitution mapping:
```
['1','2','3','4','5','6','7','8','9','0','@','#','$','z','y','x','w','v','u','t','s','r','q','p','o','n']
```
Original Character Set:
```
['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
```
```cipher1.txt``` and ```cipher2.txt``` contain the two cipher texts that need to be decrypted.\
\
I have implemented Frequency Analysis to break the cipher. 
Below are the original texts and their respective keys:
#### Cipher1.txt:
```
a disadvantage of the general monoalphabetic cipher is that both sender
and receiver must commit the permuted cipher sequence to memory.  a
common technique for avoiding this is to use a keyword from which the
cipher sequence can be generated.  for example, using the keyword cipher,
write out the keyword followed by unused letters in normal order and
match this against the plaintext letters.  make reasonable assumptions
about how to treat redundant letters and excess letters in the memory
words and how to treat spaces and punctuation.  indicate what your
assumptions are.  note, the message is from the sherlock holmes novel,
the sign of four.
```
#### Key for Cipher1.txt:
```
v : a, 9 : e, o : t, q : h, 5 : i, y : s, $ : o, 2 : r, @ : n,
8 : d, 6 : v, 7 : g, p : f, u : l, 0 : m, 3 : p, p : f, t : c,
1 : b, s : u, 4 : q, x : y, w : k, # : w, r : x, z : z
```
#### Cipher2.txt:
```
defeated and leaving his dinner untouched, he went to bed.  that night
he did not sleep well, having feverish dreams, having no rest.  he
was unsure whether he was asleep or dreaming.  conscious, unconscious,
all was a blur.  he remembered crying, wishing, hoping, begging, even
laughing.  he floated through the universe, seeing stars, planets,
seeing earth, all but himself.  when he looked down, trying to see
his body, there was nothing.  it was just that he was there, but he
could not feel anything for just his presence.
```
#### Key for Cipher2.txt:
```
q : e, 4 : l, 1 : a, n : h, 9 : v, r : i, y : n, p : g, z : d,
t : r, $ : o, @ : t, v : s, 7 : b, 5 : w, # : u, 8 : p, 3 : c,
s : m, w : f, 2 : y, 6 : k, x : j, 0 : z, u : q, o : x
```
### README:
```
$ python3 substitutioncrack.py cipher1.txt
OR
$ python3 substitutioncrack.py cipher2.txt
```
Output is shown on the terminal.

## Birthday Attack
### To-Do:
Implement the birthday attack against SHA-3 with smaller length of the hash output as follows:
- Given the length (in bits) of the hash output d, write a program which returns a tuple (s1 , s2 , h, m, n) where s1 and s2 are two strings of the same length and with the same hash output h, m is the largest memory (in bits) required to store the strings during the execution of the program, and n is the number of attempted/tested string pairs to find the collision.
- For each value of d between 1 and 24 bits, output three tuples with colli- sions.
- Compute the average number of attempts n<sub>avg</sub> and average memory m<sub>avg</sub>.
- Draw a plot where X-axis represents the length of the hash output d and
Y-axis represents the average number of attempts n<sub>avg</sub>.
- Draw another plot where X-axis represents the length of the hash output
d and Y-axis represents the average memory m<sub>avg</sub>.

### Plots:
The plots are for strings of length = 10.\
![alt text](https://github.com/aarunishsinha/Basic-Cryptanalysis-and-Encryption/blob/main/Birthday%20Attack/plotm1.jpg)
![alt text](https://github.com/aarunishsinha/Basic-Cryptanalysis-and-Encryption/blob/main/Birthday%20Attack/plotn1.jpg)
### README:
```
$ python3 birthdayattack.py <length of string>
```

## Cracking RSA
### To-Do:
Crack RSA for small values of n as follows:
- Given a number n from the file ```nlist.txt```, compute the prime factors p and
q.
- Record the time taken t to obtain these prime factors.
- Compute the public and private keys.
- Given the message M in the file ```plaintext.txt```, use the public key to encrypt the message M to ciphertext C.
- Decrypt the obtained ciphertext C back to the plaintext to validate your code.

### Prime Factorisation
For factorizing the numbers given in ```nlist.txt```, I have implemented Pollard Rho’s algorithm.\
My implementation can factorize upto 124467766935600336959819416267497 (112th number in the list) within 5 minutes.
![alt text](https://github.com/aarunishsinha/Basic-Cryptanalysis-and-Encryption/blob/main/Cracking%20RSA/plot.jpg)

### Cracking RSA
My implementation of RSA can successfully encrypt and decrypt till the 94th number in the list. After that it fails while decryption due to the limitations of the modulo operator in python.\
For encryption, first I converted each character in ```plaintext.txt``` to its ASCII decimal representation. I have stored these values in an array and the performed encryption and decryption on each element of the array.

### README:
```
python3 crack.py n plaintext.py
```
