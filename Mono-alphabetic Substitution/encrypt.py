# Import libraries
import random

# Generate key
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ', '1','2','3','4','5','6','7','8','9','0','.',',','!', "'", '"']
alphabetShuffle = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(alphabetShuffle)
alphabetShuffle.extend([' ', '1','2','3','4','5','6','7','8','9','0','.',',','!', "'", '"'])
print(alphabet)
print(alphabetShuffle)

# Get phrase from user
phrase = str(input("Enter phrase: ")).lower()

# Convert to cypher
newPhrase = list(phrase)

counter = 0
key = []

while (counter < len(phrase)):
	n = alphabet.index(newPhrase[counter])
	key.append(alphabetShuffle[n])
	counter = counter + 1

encrypted = ''.join(key)
print(encrypted)
