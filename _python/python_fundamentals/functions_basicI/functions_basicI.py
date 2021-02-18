#1
# def a():
#     return 5
# print(a())
# diagram↓
# A: print 5

#2
# def a():
#     return 5
# print(a()+a())
# diagram↓
# a() = 5
# A: print 10

#3
# def a():
#     return 5
#     return 10
# print(a())
# diagram↓
# a() = 5
# A: print 5

#4
# def a():
#     return 5
#     print(10)
# print(a())
# diagram↓
# a() = 5
# A: print 5

#5
# def a():
#     print(5)
# x = a()
# print(x)
# diagram↓
# A: print 5

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
# diagram↓
# a(1,2) => print 3 return None
# a(2,3) = print 5 return None
# A: TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# diagram↓
# "2"+"5"
# A: print 25

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 1
#     else:
#         return 10
#     return 7
# print(a())
# diagram↓
# a() => print 100, return 10
# A: print 100, 10

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# diagram↓
# (a(2,3)) => return 7
# (a(5,3)) => return 14
# (a(2,3) + a(5,3)) => (7+14) = 21 
# A: print 7 14 21

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
# diagram↓
# a(3,5) => return (3+5) = 8
# A: print 8

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
# diagram↓
# print(b) = 500
# print(b) = 500
# a() => b = 300 => print(b) = 300 
# print(b) = 500
# A: print 500 500 300 500

#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# diagram↓
# print(b) = 500
# print(b) = 500
# a() => b = 300 => print(b) = 300、return = 300 
# print(b) = 500
# A: print 500 500 300 500

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# diagram↓
# print(b) = 500
# print(b) = 500
# b = a() => b = 300 => print(b) = 300、return = 300 => b = 300  
# print(b) = 300
# A: print 500 500 300 300

#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# diagram↓
# a() => print 1 => b() => print 3 => print 2
# A: print 1 3 2

# #15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)
# diagram↓
# y = a()  
# a() => print 1  
# x = b() => print 3 x=5
# print(x) => print 5
# y = a() => return 10 => y=10
# A: print 1 3 5 10

