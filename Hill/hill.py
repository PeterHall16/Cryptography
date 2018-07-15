# Current version only encrypts - 6/26/2018 (M/D/Y)
# Import libraries
import numpy as np
import numpy.linalg
import itertools
from itertools import islice
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style



def encrypt():
	# Define variables
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	numericPhrase = []
	counter = 0
	check = 0

	# Get phrase
	phrase = str(input("Enter phrase: ")).upper()
	phrase =  list(phrase)
	print(phrase)

	# Get matrix dimensions
	# dimension = int(input("Enter integer key dimension: "))

	# # Split phrase
	# def chunk(it, size):
	#     it = iter(it)
	#     return iter(lambda: tuple(islice(it, size)), ())

	# phrase = list(chunk(phrase, 3))
	# print(phrase)

	while (check == 0):
		randomMatrix = np.random.randint(low = 0, high = 25, size = (len(phrase),len(phrase)))
		key = np.matrix(randomMatrix)
		print(key)

		# Check if determinant is nonzero 
		# Range set at +/- 1 because sometimes determinant will be a very small number
		# even though it should be 0.
		if (np.linalg.det(key) > 1 or np.linalg.det(key) < -1):
			check = 1
			break

	while (counter < 26):
		numericPhrase.append(alphabet.index(phrase[counter]))
		counter = counter + 1
		if (len(numericPhrase) ==  len(phrase)):
			counter = 0
			break

	print(Fore.GREEN + Style.BRIGHT + "Numeric Phrase:")
	print(numericPhrase)

	# Convert phrase to matrix
	phraseArray = np.reshape(numericPhrase, (len(phrase), 1))
	phraseMatrix = np.matrix(phraseArray)

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

	finalLetters = []
	counter = 0

	while (counter < len(phrase)):
		finalLetters.append(alphabet[merged[counter]])
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






