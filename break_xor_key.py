# -*- coding: utf-8 -*-

'''
break_xor_key.py
Yoji Watanabe

Script to find the key used in a XOR cipher given the input text and the 
encrypted text.
'''

import argparse

parser = argparse.ArgumentParser(description='Script to find the key used in a \
	xor cipher given the input text and the encrypted text')
parser.add_argument('f_encrypted', metavar='encrypted_text_file', type=str, \
	help='Input text')
parser.add_argument('f_decrypted', metavar='decrypted_text_file', type=str, \
	help='Output/encrypted text')
args = parser.parse_args()

# getData(enInput, deInput)
# Function to retrieve encrypted data and decrypted data from the given input
# files.
# Input:  enInput - string to path of the input file
# 		  deInput - string to path of the output file
# Output: two-element array with first element encrypted data, second element 
# 		  decrypted data
def getData(enInput, deInput):
	encrypt = open(enInput, 'r').read().split();
	decrypt = open(deInput, 'r').read();

	return [encrypt, decrypt]

# getKey(encrypt, decrypt)
# Function to calculate the key used to encrypt a string with an xor cipher
# files.
# Input:  encrypt - string with encrypted data
# 		  decrypt - string with decrypted data
# Output: string with the key used to encrypt data
def getKey(encrypt, decrypt):
	key = ''
	for i in range(0, len(encrypt)):
		key = key + unichr(int(encrypt[i], 16) ^  \
			  ord(decrypt[i % len(decrypt)]));

	return key

# def cleanKey(keyString):
# Returns the key from a larger substring containing multple keys.
# Input:  keyString - string with multiple instances of key to get key from
# Output: string with key
def cleanKey(keyString):
    for x in range(1, len(keyString)):
        tempKey = keyString[:x]

        if tempKey * (len(keyString) // len(tempKey)) + \
          (tempKey[:len(keyString) % len(tempKey)]) == keyString:
            return tempKey

if __name__ == '__main__':
	[encrypt, decrypt] = getData(args.f_encrypted, args.f_decrypted)
	key = getKey(encrypt, decrypt)
	key = cleanKey(key)


	print 'Text to decrypt:\t'  + ''.join(encrypt)
	print 'Decrypted text:\t\t' + decrypt
	print '########################################'
	print '\tDecrypted key:\t\t'  + key
	print '########################################'