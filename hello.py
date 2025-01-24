def CurrDate():
	import datetime
	now = datetime.datetime.now() 
	print ("Current date and time : ")
	print (now.strftime("%Y-%m-%d %H:%M:%S"))
	pass

#write me a function for fibonacci series
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a if n else 0

def Fibonacci(n):
    if n < 0:
        return None
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a if n > 0 else 0

print(Fibonacci(9))

#write me a function for factorial
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

#write unit test cases for the above function
import unittest
class TestFactorial(unittest.TestCase):
	def test_factorial(self):
		self.assertEqual(factorial(5), 120)
		self.assertEqual(factorial(6), 720)
		self.assertEqual(factorial(7), 5040)
		self.assertEqual(factorial(0), 1)
		self.assertEqual(factorial(1), 1)
		self.assertEqual(factorial(2), 2)


#Write me a code multiply two numbers
def multiply(a, b):
	return a*b



