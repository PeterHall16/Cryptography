# Define variables and certain arrays
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
counter = 0
numericKey = []
numericPhrase = []

# Get key
key = str(input("Enter key (letters only, no spaces or punctuation): ")).upper()
key = list(key)

while (counter < 26):
	numericKey.append(alphabet.index(key[counter]))
	print(numericKey)
	counter = counter + 1
	if (len(numericKey) == len(key)):
		counter = 0
		break