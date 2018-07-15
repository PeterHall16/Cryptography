# Import libraries
import numpy as np
import numpy.linalg

def program():
	# Define variables and arrays
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','.',',','"','?',' ','!','+','-','=','*','/','(',')','@','#','$','%','^','&','_','`','~','<','>',':',';','[',']','{','}','|']
	numericAlphabet = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	key = []
	counter = 0
	numericPhrase = []
	encrypted = []
	decrypted = []

	# Select encryption or decryption
	toggle = str(input("Encrypt(1) or decrypt(2)?"))

	# Get phrase to encrypt/decrpyt, equation
	phrase = list(str(input("Input phrase: ")).upper())
	print('Enter "a" and "b" values in the form (ax + b). "a" must be coprime with 26 (alphabet length)')
	a = int(input("A: "))
	b = int(input("B: "))

	# Convert to numbers
	while (counter < len(phrase)):
		n = alphabet.index(phrase[counter])
		numericPhrase.append(n)
		counter = counter + 1

		if (len(numericPhrase) == len(phrase)):
			counter = 0
			n = 0
			break

	print("Numeric phrase:  ")
	print(numericPhrase)

	# Create key
	while (counter < 26):
		key.append(np.remainder((numericAlphabet[counter] * a + b), 26))
		counter = counter + 1

	print("Key:")
	print(key)

	def encrypt():
		counter = 0
		final = []
		
		while (counter < len(alphabet)):
			if (numericPhrase[counter] < 26):
				encrypted.append(key[numericPhrase[counter]])
				final.append(alphabet[encrypted[counter]])
			else:
				encrypted.append(alphabet[counter])
				final.append(alphabet[numericPhrase[counter]])
			counter = counter + 1

			if (len(phrase) == len(encrypted)):
				break
				counter = 0

		final = ''.join(final)
		print(final)
		quit()

	def decrypt():
		counter = 0
		final = []

		while (counter < len(alphabet)):
			if (numericPhrase[counter] < 26):
				decrypted.append(key.index(numericPhrase[counter]))
				final.append(alphabet[decrypted[counter]])
			else:
				decrypted.append(alphabet[counter])
				final.append(alphabet[numericPhrase[counter]])
			counter = counter + 1

			if (len(phrase) == len(decrypted)):
				break
				counter = 0

		final = ''.join(final)
		print(final)
		quit()

	# Call function
	if (toggle == "1"):
		encrypt()
	if (toggle == "2"):
		decrypt()
	else:
		print("Please enter a valid response.")

program()