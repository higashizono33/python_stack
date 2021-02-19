# 1. Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x = [ [5,2,3], [10,8,9] ] 
# my function↓
# def changeValue(num, idx_1, idx_2):
#     x[idx_1][idx_2] = num
# changeValue(15, 1, 0)
# print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# my function↓
# def changeLastName(name, idx_1, dict_1):
#     students[idx_1][dict_1] = name
# changeLastName("Bryant", 0, "last_name")
# print(students)

# In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# my function↓
# def changeSportDirectory(name, dir_name, idx_1):
#     sports_directory[dir_name][idx_1] = name
# changeSportDirectory("Andres", "soccer", 0)
# print(sports_directory)

# Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ]
# my function↓
# def changeValue(value, list_loc, dir_name):
#     list_loc[dir_name] = value
# changeValue(30, z[0], 'y')
# print(z)


# 2. Iterate Through a List of Dictionaries
# should output: (it's okay if each key-value pair ends up on 2 separate lines;copy
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# my function↓
# def iterateDictionary(list_students):
#     for i in range(0, len(list_students)):
#         output = "first_name - " + list_students[i]['first_name'] + ", last_name - " + list_students[i]['last_name']
#         print(output)

# iterateDictionary(students)


# 3. Get Values From a List of Dictionaries
# iterateDictionary2('first_name', students) should output:
# Michael John Mark KB
# iterateDictionary2('last_name', students) should output:
# Jordan Rosales Guillen Tonel
# my function↓
# def iterateDictionary2(key_name, some_list):
#     for i in range(0, len(some_list)):
#         output = some_list[i][key_name]
#         print(output)

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# my function↓
# def printInfo(some_list):
#     for i in range(0, len(some_list)):
#         print(len(some_list[list(some_list)[i]]), list(some_list)[i].upper())
#         for j in range(0, len(some_list[list(some_list)[i]])):
#             print(some_list[list(some_list)[i]][j]) 

# printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon