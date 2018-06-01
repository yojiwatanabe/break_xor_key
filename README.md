# break_xor_key.py
A simple Python script to find the key used in a XOR cipher. With a cleartext message and its XOR encrypted message, you can use this tool to find the key used to encode the messages. This can allow you to break future messages using the same XOR cipher key as well as encrypt your own messages with the same method.

#### Running the program:
1. Ensure you have files containing the cleartext and encrypted message. Ensure files have only the parts of cipher, and no extra newlines, etc.
	- example decrypted message file:
	```
	hey there secret spy
	```
	- example encrypted message file:
	```
	07 0d 17 4f 55 07 0d 1c 0a 01 1c 0d 0d 1d 44 1b 48 1d 1f 58
	```
	note: encrypted messages should be stored in hexadecimal separated by a space (' ')
2. Run
	```
	$ python break_xor_key.py enc dec
	Text to decrypt:	070d174f55070d1c0a011c0d0d1d441b481d1f58
	Decrypted text:		hey there secret spy
	########################################
		Decrypted key:		ohno!
	########################################
	```

#### Disclaimer:
This script is for educational purposes only. The author, Yoji Watanabe, is not responsible for the use of this script, repository, or any information contained inside it. Any action the user takes with this script (or any information) in it is solely the user's responsibility. Use at your own risk.