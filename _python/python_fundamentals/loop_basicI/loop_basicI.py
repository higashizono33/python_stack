# for i in range(0, 151, 1):
#     print(i)
# for i in range(5, 1001, 5):
#     print(i)
# for i in range(1, 101):
#     if(i % 10 == 0):
#         print("Coding Dojo")
#     elif(i % 5 == 0):
#         print("Coding")
#     else:
#         print(i)
# sum = 0
# for i in range(0, 500001, 1):
#     if(i % 2 == 1):
#         sum += i
# print(sum)
# count = 2018
# while count > 0:
#     print(count)
#     count -= 4
lowNum = 2
highNum = 9
mult = 3
i = mult

while mult <= highNum:
    if(mult >= lowNum):
        print(mult)
    mult += i
