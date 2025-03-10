## Password Cracker

This is a simple brute-force password cracking function implemented in python which uses hashlib library to compare two file, a list of common passwords (https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt) and a hashed MD5 password file. This function finds passwords comparing both the files and prints the output. 

- the passwd.encode(): converts the string passwd into bytes. We do this because hashing functions in Python require bytes-like objects as input.

- Hashing with MD5: hashlib.md5() applies the MD5 hashing algorithm to the encoded bytes. 

- Hexadecimal Representation: .hexdigest() converts the resulting hash bytes into a hexadecimal string.

We do this because in order to find the right password, we need to compare the content from both the plain-text file and the hashed file 
to figure out which ones are matching.