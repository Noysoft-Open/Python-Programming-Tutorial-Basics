# integer
number = 2
print("integer: %s" % number)
number = -1
print("integer: %s" % number)
number = 12E4
print("integer: %s" % number)
number = -87.7e100
print("integer: %s" % number)

# float
numfloat = 2.0
print("float: %s" % numfloat)

# complex number
i = 1j
print("complex number: %s" % i)
i = 3 + 1j
print("complex number: %s" % i)

# range
num = range(0, 5)
print("Range: %s" % num)

# ramdom
# import is a pre defined keyword that let the interpreter include the random package
import random
rand_num = random.randrange(1, 10)
print("Random: %s" % rand_num)

# string
message = "Hello"
print("string: %s" % message)

# array list
position = [1, 2]
print("array list: %s" % position)

# tuple
computer = ("apple", "ibm")
print(computer)

# dictionary
member = {
    'name' : 'Jayson',
    'age' : '26'
}
print(member)

# set
cars = {"Ferrari", "Chevrolet", "Toyota"}
print(cars)

# frozen set
cars = frozenset({"Ferrari", "Chevrolet", "Toyota"})
print(cars)

# boolean
open = True
print(open)

# bytes
message = b"Hello"
print(message)

# byte array
bytearry = bytearray(5)
print(bytearry)

# memory view
memview = memoryview(bytes(5))
print(memview)

# None
m = None
print(m)
