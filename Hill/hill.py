# Current version only encrypts - 6/26/2018 (M/D/Y)
# Import libraries
import numpy as np
import numpy.linalg
import math
import itertools
from itertools import islice
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

def encrypt():
	# Define variables
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	numericPhrase = []
	appendedList = []
	counter = 0
	check = 0
	key = []

	# Get phrase
	phrase = str(input("Enter phrase: ")).upper()
	phrase =  list(phrase)
	print(phrase)

	# Ask to generate or input key
	toggleKey = str(input("Enter key(1) or generate one randomly(2)?"))

	# print(Back.YELLOW + Style.BRIGHT +"As of 7/16/2018 (M/D/Y), key dimension must be a factor or the phrase length. Will fix soon.")
	keyDimension = int(input("Enter key length (Must be a perfect square.): "))
	keyDimension = int(math.sqrt(keyDimension))
	
	if (toggleKey == "1"):
		# User inputed key
		keyValues = list(str(input("Enter keyword phrase.")).upper())

		while (counter < len(keyValues)):
			n = alphabet.index(keyValues[counter])
			key.append(n)
			counter = counter + 1

			if (len(key) == len(keyValues)):
				counter = 0
				n = 0
				break

		matrixBase = np.reshape(key, (keyDimension, keyDimension))
		key = np.matrix(matrixBase)

	if (toggleKey == "2"):
		# Generate random key
		while (check == 0):
			randomMatrix = np.random.randint(low = 0, high = 25, size = (keyDimension,keyDimension))
			key = np.matrix(randomMatrix)

			# Check if determinant is nonzero 
			# Range set at +/- 1 because sometimes determinant will be a very small number even though it should be 0.
			if (np.linalg.det(key) > 1 or np.linalg.det(key) < -1):
				check = 1
				break

		# Fix if invalid response entered
		print(Fore.GREEN + Style.BRIGHT + "key:")
		print(key)

	determinant = np.linalg.det(key).round()
	print("Determinant:")
	print(determinant)

	if (determinant == 0):
		print("Determinant = 0, CHANGE KEY")
	elif ((determinant % len(alphabet)) == 0):
		print("Determinant disivible by alphabet length, CHANGE THE KEY!")

	while (counter < 26):
		numericPhrase.append(int(alphabet.index(phrase[counter])))
		counter = counter + 1
		if (len(numericPhrase) ==  len(phrase)):
			counter = 0
			break

	# Split phrase
	def chunk(it, size):
	    it = iter(it)
	    return iter(lambda: tuple(islice(it, size)), ())

	numericPhrase = list(chunk(numericPhrase, keyDimension))
	print(numericPhrase)
	segments = len(numericPhrase)
	counter = 0

	while (counter < segments):
		print(Fore.GREEN + Style.BRIGHT + "----------------------------------------")
		a = list(numericPhrase[counter])
		print(a)
		counter = counter + 1

		if (len(a) < keyDimension):
			while (len(a) < keyDimension):
				a.append(25)

		# Convert phrase to matrix
		phraseArray = np.reshape(a, (keyDimension, 1))
		phraseMatrix = np.matrix(phraseArray)

		print(phraseMatrix)

		# Multiply key and phrase matrices
		encipheredVector = key * phraseMatrix 
		print(Fore.GREEN + Style.BRIGHT + "Enciphered vector:")
		print(encipheredVector)

		# Modulus
		final = np.remainder(encipheredVector, 26)
		print(Fore.GREEN + Style.BRIGHT + "Modulated:")
		print(final)

		# Convert back to text
		finalNumeric = final.tolist()
		merged = list(itertools.chain(*finalNumeric))
		print(merged)

		appendedList.append(merged)

	print(Fore.GREEN + Style.BRIGHT + "----------------------------------------")

	print(appendedList)
	finalLetters = []
	counter = 0

	total = []
	for i in appendedList:
		total += i

	print(total)

	while (counter < len(total)):
		finalLetters.append(alphabet[total[counter]])
		counter = counter + 1

	finalLetters = ''.join(finalLetters)
	print(Fore.GREEN + Style.BRIGHT + "Encrypted: " + Fore.CYAN + finalLetters)
	quit()

def decrypt():
	# Define variables
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	numericPhrase = []
	keyList = []
	counter = 0
	check = 0

	# Get phrase
	phrase = str(input("Enter phrase: ")).upper()
	phrase =  list(phrase)
	print(phrase)

	# Get matrix dimensions
	dimension = int(input("Enter integer key dimension: "))

	# Get key from user
	while (counter < dimension * dimension):
		key = str(input("Enter key (in list form): "))
		keyList.append(key)
		print(key)
		print(keyList)
		counter = counter + 1

	print("decrypting...")
	quit()

# Select operation
def toggle():
	choice = str(input("Encypt(1) or decrypt(2)? ")).upper()
	if (choice == "1"):
		encrypt()
	if (choice == "2"):
		decrypt()
	else:
		print(Back.RED + Style.BRIGHT + "Please enter a valid response.")
		toggle()

toggle()