# Define variables and certain arrays
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
counter = 0
numericKey = []
extendedKey = []
numericPhrase = []

def crypt():
	# Define local variables
	counter = 0
	final = [int(numericPhrase[i]) + int(extendedKey[i]) for i in range(len(numericPhrase))]
	# Select to encrypt or decrypt
	toggle = str(input("Encrypt(1) or decrypt(2) the phrase? "))
	if (toggle == '1'): 
		# Add lists
		print(final)

		# Convert back to letters
		finalLetters = []

		while (counter < len(phrase)):
			finalLetters.append(alphabet[final[counter]])
			counter = counter + 1

		print("Encrypted: " + ''.join(finalLetters))
		quit()
	if (toggle == '2'):
		decryptFinal = [int(numericPhrase[i]) - int(extendedKey[i]) for i in range(len(numericPhrase))]
		print(decryptFinal)
		finalDecryptLetters = []
		while (counter < len(phrase)):
			finalDecryptLetters.append(alphabet[decryptFinal[counter]])
			counter = counter + 1

		print("Decrypted: " + ''.join(finalDecryptLetters))
		quit()
	else:
		print("Please enter a valid response.")
		crypt()

# Get key
key = str(input("enter key (letters only, no spaces): ")).upper()
key = list(key)

while (counter < 26):
	numericKey.append(alphabet.index(key[counter]))
	print(numericKey)
	counter = counter + 1
	if (len(numericKey) == len(key)):
		counter = 0
		break

# Get phrase to encrypt
phrase = list(str(input("enter phrase to encrypt/decrypt: ")).upper())

while (counter < 26):
	numericPhrase.append(alphabet.index(phrase[counter]))
	print(numericPhrase)
	counter = counter + 1
	if (len(numericPhrase) ==  len(phrase)):
		counter = 0
		break

while (len(extendedKey) < len(phrase)):
	extendedKey.append(str(numericKey[counter]))
	print(extendedKey)
	print(counter)
	counter = counter + 1
	if (counter >= len(key)):
		counter = 0

crypt()