# Python Basics Chapter 5:
# ========================

# 1. Introduction To List

# A list is a ordered collection of items.

# We can store anything in lists such as int, float, string etc.

# numbers = [1, 2, 3]
# print(numbers)
# print(numbers[0])

# words = ["one", "two", 'three']
# print(words)
# print(w6ords[:2])
# print(words[:])

# mixed = [1, "two", None]
# print(mixed)
# print(mixed[-1])

# mixed[2] = "three"
# print(mixed)

# mixed[2] = 3
# print(mixed)

# mixed[0:3] = ["a", "b", "c"]
# print(mixed)

# mixed[0:3] = [0, 1, 2]
# print(mixed)

# 2. Add Data To List

# append method always add item at the last

# fruits = ["grapes", "mangos"]

# fruits.append("apple")
# print(fruits)

# fruits = []

# fruits.append("mangos")
# fruits.append("grapes")
# print(fruits)

# 3. More Methods To Add Data

# insert method - add item at any position
# join (concatenate) two list
# extend method 
# difference between append and extend method

# fruits1 = ['mango', 'orange']

# fruits1.insert(1, 'grapes')
# print(fruits1)

# fruits2 = ["grapes", "pineapple"]

# fruits = fruits1 + fruits2
# print(fruits)

# fruits1.append(fruits2)
# print(fruits1)
# print(fruits2)
 
# fruits1.extend(fruits2)
# print(fruits1)
# print(fruits2)

# 4. Delete Data From List

# pop method
# del operator/statement
# remove method

# fruits = ['mango', 'orange'  , 'apple', 'kiwi', 'banana', 'pineapple', 'banana']

# fruits.pop()
# print(fruits)

# fruits.pop(1)
# print(fruits)

# del fruits[2]
# print(fruits)

# fruits.remove("banana")
# print(fruits)

# 5. In Keyword With List

# fruits = ['mango', 'orange', 'apple', 'kiwi', 'banana', 'pineapple']

# if 'apple' in fruits:
#     print("apple is present")
# else:
#     print("apple is not present")

# fruits = ["Apple","orange", "Banana"]
# if "kiwi" in fruits:
#     print("orange is present")
# else:
#     print("orange is not prsent")



# 6. Some More List Methods

# count
# sort method
# sorted function
# reverse
# clear
# copy

# fruits = ['mango', 'orange', 'apple', 'kiwi', 'banana', 'pineapple', 'mango']

# print(fruits.count('mango'))

# fruits.sort()
# print(fruits)

# numbers = [3, 5, 1, 9, 10]

# numbers.sort()
# print(numbers)

# print(sorted(fruits))
# print(sorted(numbers))

# fruits = sorted(fruits)
# numbers = sorted(numbers)

# print(fruits)
# print(numbers)

# numbers.clear()
# print(numbers)

# numbers_copy = numbers.copy()
# print(numbers_copy)

# numbers.reverse()
# print(numbers)

# numbers = list(reversed(numbers))

# print(numbers)

# 7. Is Vs Equals

# compare lists
# ==, is

# fruits1 = ['mango', 'orange', 'apple']
# fruits2 = ['mango', 'orange', 'apple']

# if fruits1 is fruits2:
#     print("fruits1 is fruits2")
# else:
#     print("fruits1 is not fruits2")

# if fruits1 == fruits2:
#     print("fruits1 is fruits2")
# else:
#     print("fruits1 is not fruits2")

# print(id(fruits1))
# print(id(fruits2))

# 8. Join And Split Method

# split method
# convert string to list

# user_info = 'anshul 24'
# user_info_list = user_info.split()
# print(user_info_list)

# user_info = input("Your name and age separated by comma : ")
# name, age = user_info.split(',')
# print(name)
# print(age)

# join method
# convert list to string

# print(' '.join(user_info_list))
# print(','.join(user_info_list))

# 9. List Vs Array

# arrays are more faster than lists but lists are more flexible.

# c, c++, java
# In arrays, we can store only a fixed type of data.

# python
# In lists, we can store any type of data.
# python array module - fix data type. 
# numpy arrays - binding with c libraries.

# javascript
# arrays = lists

# 10. List Vs String

# strings are immutable

# s = ('python')

# t = s.replace('p', 'j')
# print(t)
# print(s)

# lists are mutable

# l = ['one', 'two', 'three']

# l.pop()
# print(l)

# l.append('four')
# print(l)

# 11. Looping In List

# fruits = ['mango', 'orange', 'apple', 'kiwi', 'banana', 'pineapple']

# for fruit in fruits:
#     print(fruit)

# for fruit in fruits:
#     print(fruit, end=" ")

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# i = 0
# while i < len(fruits):
#     print(fruits[i], end=" ")
#     i += 1

# 12. List Inside List

# 1 list -> 3 items -> 3 lists

# 2D

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 3D

# matrix = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

# print(matrix[0][0])
# print(matrix[1][2])
# print(matrix[2][2])

# print(matrix[0][0][0])
# print(matrix[1][2][0])
# print(matrix[2][2][0])

# for i in matrix:
#     print(i)

# for i in matrix:
#     print(i, end=" ")

# for i in matrix:
#     for j in i:
#         print(j)

# for i in matrix: 
#     for j in i:
#         print(j, end=" ")

# for i in matrix:
#     for j in i:
#         for k in j:
#             print(k)

# print(matrix[1][1])
# print(matrix[2][0])

# s = "anshul"
# print(type(s))

# print(type(matrix))

# Using While Loop -

# i = 0
# while i < len(matrix):
#     j = 0
# while j < len(matrix[i]):
#     k = 0
# while k < len(matrix[i][j]):
#     print(matrix[i][j][k])
#     k += 1
#     j += 1
#     i += 1  

# 13. More About Lists

# generate lists with range functions
# something more about pop method
# index method
# pass list to a function

# numbers = list(range(1, 11))
# print(numbers)

# popped_item = numbers.pop()
# print(popped_item)

# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 5, 7, 8, 1]
# print(numbers.index(1))
# print(numbers.index(1, 1))
# print(numbers.index(1, 5))
# 
# # #print(numbers.index(1, 11, 14)) # error

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers = list(range(1, 11))

# def negative_list(numbers):
# negative = []
    
# for i in numbers:
# negative.append(-i)
# return negative

# print(negative_list(numbers))

# 14. Exercise - 1

# define a function which will take list containing numbers as input
# and return list containing square of every elements.

# 15. Exercise - 1 Solution

#def square_list(l):
    #squares = []
     
    #for i in l:
        #squares.append(i**2)
    
#     return squares

#print(square_list([1, 2, 3, 4, 5]))

# numbers = list(range(1, 11))
#print(square_list(numbers))

# 16. Exercise - 2

# define a function which will take list as a argument and this 
# function will return a reversed list.

# 17. Exercise - 2 Solution

# def reverse_list(l):
#     l.reverse()
#      return l

# def reverse_list(l):
#     return list(reversed(l))

# def reverse_list(l):
#     return l[::-1]

# def reverse_list(l):
#     reverses = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         reverses.append(popped_item)
    
#     return reverses

# numbers = list(range(1, 6))
# print(reverse_list(numbers))

# 18. Exercise - 3

# define a function that take list of words as argument and return
# list with reverse of every element in that list.

# 19. Exercise - 3 Solution

# def reverse_elements(l):
#     reversed_words = []
#     for word in l:
#         reversed_words.append(word[::-1])
    
#     return reversed_words

# words = ['abc', 'xyz', '123']
# print(reverse_elements(words))

# 20. Exercise - 4

# filter odd even
# define a function
# input
# list ---> [1, 2, 3, 4, 5, 6, 7]
# output -> [[1, 3, 5, 7], [2 , 4, 6]]

# 21. Exercise - 4 Solution

# def filter_odd_even(l):
#     mixed = []
#     odds = []
#     evens = []
    
#     for num in l:
#           if num % 2 == 0:
#             evens.append(num)
#         else:
#             odds.append(num)
    
#     mixed.append(odds)
#     mixed.append(evens)
    
#     return mixed

# print(filter_odd_even([1, 2, 3, 4, 5, 6, 7]))

# 22. Exercise - 5

# Common elements finder function

# define a function which takes 2 lists as input and return a list
# which contains common elements of both lists.

# 23. Exercise - 5 Solution

# def common_elements_finder(l1, l2):
#     commons = []
    
#     for i in l1:
#         if i in l2:
#             commons.append(i)
    
#     return commons

# print(common_elements_finder([1, 2, 5, 8], [1, 2, 7, 6]))

# 24. Min And Max Function

# numbers = [6, 60, 2]

# print(min(numbers))
# print(max(numbers))

# def greatest_diff(l):
#     return max(l) - min(l)

# print(greatest_diff(numbers))

# 25. Exercise - 6

# define a function for finding the number of sublists in a 
# list.
# input : [1, 2, 3, [1, 2], [3, 4]] 
# output : 2

# 26. Exercise - 6 Solution

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1

    return count

# lists = [1, 2, 3, [1, 2], [3, 4]]
# print(sublist_counter(lists))
