import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        self.result += num
        for x in nums:
            self.result += x
        return self

    def subtract(self, num, *nums):
        # your code here
        self.result -= num
        for y in nums:
            self.result -= y
        return self

# create an instance:
# md = MathDojo()

# to test:
class MathDojoTests(unittest.TestCase):
    def setUp(self):
        # unittest.TestCase.setUp(self)
        self.md = MathDojo()
    def testOne(self):
        self.assertEqual(self.md.add(2).add(2,5,1).subtract(3,2).result, 5)
    def testTwo(self):
        self.assertEqual(self.md.add(1).add(2,5,6).subtract(3,2,5).result, 4)
    def testThree(self):
        self.assertEqual(self.md.add(2,1,3).add(5,1).subtract(1,10).result, 1)
    def testFour(self):
        self.assertEqual(self.md.add(5,6).add(1).subtract(3,2).result, 7)
    def testFive(self):
        self.assertEqual(self.md.add(4,9).add(8,5,1).subtract(10,12).result, 5)
    
    # def tearDown(self):
    #     print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests


# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)	# should print 5
# run each of the methods a few more times and check the result!
# y = md.add(1).add(2,5,6).subtract(3,2,5).result
# print(y)
# z = md.add(2,1,3).add(5,1).subtract(1,10).result
# print(z)
# a = md.add(5,6).add(1).subtract(3,2).result
# print(a)
# b = md.add(4,9).add(8,5,1).subtract(10,12).result
# print(b)