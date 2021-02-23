# import the python testing framework
import unittest

# reverseList - Write a function that reverses the values in the list (without creating a temporary array).
# Example: reverseList([1,3,5]) should return [5,3,1]
# Example Test: assertEqual( reverseList([1,3,5]), [5,3,1] )
# Add at least 3 other test cases
def reverseList(arr):
    for i in range(int(len(arr)/2)):
        x = arr[i]
        arr[i] = arr[len(arr)-(1+i)]
        arr[len(arr)-(1+i)] = x
    return arr
    
# class ReverseListTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(reverseList([1,3,5]), [5,3,1])
#     def testTwo(self):
#         self.assertEqual(reverseList([1,3,5]), [5,3,1])
#     def testThree(self):
#         self.assertEqual(reverseList([1,3,5]), [5,3,1])
    
#     def setUp(self):
#         print("running setUp")
#     def tearDown(self):
#         print("running tearDown tasks")

# if __name__ == '__main__':
#     unittest.main() # this runs our tests

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).
# Example: isPalindrome("racecar") should return True
# Example Test: assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar"))
# Example Test: assertFalse( isPalindrome("rabcr") ).
# Add at least 5 other test cases
def isPalindrome(word):
    word_lower = word.lower()
    word_list = list(word_lower)
    # print(word_list)
    for i in range(int(len(word_list)/2)):
        x = word_list[i]
        word_list[i] = word_list[len(word_list)-(1+i)]
        word_list[len(word_list)-(1+i)] = x
    if word_list == list(word_lower):
        return True
    else:
        return False

# class IsPalindromeTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(isPalindrome("racecar"), True)
#     def testTwo(self):
#         self.assertFalse(isPalindrome("rabcr"))
#     def testThree(self):
#         self.assertTrue(isPalindrome("Anna"))
#     def testFour(self):
#         self.assertTrue(isPalindrome("Civic"))
#     def testFive(self):
#         self.assertTrue(isPalindrome("Level"))
    
#     # def setUp(self):
#     #     print("running setUp")
#     # def tearDown(self):
#     #     print("running tearDown tasks")

# if __name__ == '__main__':
#     unittest.main() # this runs our tests

# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.
# Example: given 87 cents, result should be 3 quarters, 1 dime, 0 nickel and 2 pennies
# Example Test: assertEqual( coin(87), [3,1,0,2] )
# Add at least 5 other test cases

def coins(cents):
    coins = []
    quarters = int(cents / 25)
    coins.append(quarters)
    dimes = int((cents-(25 * quarters)) / 10)
    coins.append(dimes)
    nickels = int((cents-(25 * quarters + 10 * dimes)) / 5)
    coins.append(nickels)
    pennies = int((cents-(25 * quarters + 10 * dimes + 5 * nickels)) / 1)
    coins.append(pennies)

    return coins

# class CoinsTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(coins(87), [3,1,0,2])
#     def testTwo(self):
#         self.assertEqual(coins(90), [3,1,1,0])
#     def testThree(self):
#         self.assertTrue(coins(50), [2,0,0,0])
#     def testFour(self):
#         self.assertTrue(coins(40), [2,1,1,0])
#     def testFive(self):
#         self.assertTrue(coins(100), [4,0,0,2])
    
#     # def setUp(self):
#     #     print("running setUp")
#     # def tearDown(self):
#     #     print("running tearDown tasks")

# if __name__ == '__main__':
#     unittest.main() # this runs our tests

# BONUS - factorial - Write a recursive function that returns the factorial of a given number. Remember that the factorial of a number is
# the product of all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).
# Example: factorial(5) should return 120.
# Add at least 3 test cases

def factorial(num):
    x = 1
    for i in range(1, num+1):
        x = x * i
    return x

# class FactorialTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(factorial(5), 120)
#     def testTwo(self):
#         self.assertEqual(factorial(10), 3628800)
#     def testThree(self):
#         self.assertEqual(factorial(1), 1)

# if __name__ == '__main__':
#     unittest.main() # this runs our tests

# BONUS - fibonacci - Write a recursive function that accepts a number, n, and returns the nth Fibonacci number from the sequence. 
# The first two Fibonacci numbers are 0 and 1. Every number after that is calculated by adding the previous 2 numbers from the sequence. 
# (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
# Example: fibonacci(5) should return 3 (the 5th number in the sequence is 3).
# Add at least 3 test cases

def fibonacci(num):
    if num <= 1:
        return False
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        # 3: 0 + 1 = 1
        # 4: 1 + 1 = 2
        # 5: 1 + 2 = 3
        # 6: 2 + 3 = 5
        # 7: 3 + 5 = 8
        fibonacci_list = [0, 1]
        x = 0
        for i in range(2, num):
            x = fibonacci_list[i-2] + fibonacci_list[i-1]
            fibonacci_list.append(x)
        return fibonacci_list[num-1]

class FibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(5), 3)
    def testTwo(self):
        self.assertEqual(fibonacci(9), 21)
    def testThree(self):
        self.assertEqual(fibonacci(10), 34)

if __name__ == '__main__':
    unittest.main() # this runs our tests