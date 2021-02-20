#changed folder name
import random
import math
#print(randInt()) 		    # should print a random integer between 0 to 100
#my function↓
# def randInt(min=0, max=0):
#     return  math.floor(max * random.random())
# print(randInt(min=0, max=100))

#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#my function↓
# def randInt(min=0, max=50):
#     num = random.random()
#     return math.floor(max * num)
# print(randInt(max=50))

#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#my function↓
# def randInt(min=50, max=100):
#     num = random.random()
#     return math.floor(min * num) + min
# print(randInt(min=50))

#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
# def randInt(min=50, max=500):
#     num = random.random()
#     return math.floor((max-min) * num) + min
# print(randInt(min=50, max=500))

# BONUS: account for any edge cases (eg. min > max, max < 0)
# def randInt(min=0, max=0):
#     if(min > max):
#         return False
#     elif(max < 0):
#         return False
#     else:
#         num = random.random()
#         return int((max-min) * num) + min
# print(randInt(min=1, max=10))