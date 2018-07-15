import numpy as np
import numpy.linalg

from colorama import init
init()
from colorama import Fore, Back, Style

phrase = "abc"
phrase =  list(phrase)
print(phrase)

# randomMatrix = np.random.randint(low = 0, high = 25, size = (3,3))
# key = np.matrix(randomMatrix)
# key = [[0,0,0],[17,19,23],[41,43,47]]
key = np.matrix(key)
print(key)

# while (0 == 0):
# 	inverse = np.linalg.inv(key)
# 	print(inverse)

# if (numpy.isfinite(numpy.linalg.cond(key))):
#     keyInv = numpy.linalg.inv(key)
# else:
# 	print("Single")

# if linalg.cond(key) < 1/sys.float_info.epsilon:
#     i = linalg.inv(key)
# else:
#     print("Single")	

determinant = np.linalg.det(key)
print(determinant)