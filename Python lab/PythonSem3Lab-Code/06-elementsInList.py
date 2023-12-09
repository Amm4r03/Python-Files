'''
author	:	Ammar Ahmad Kidwai (2022-350-005)
topic	:	experiment 6
title   :	operations on list
'''

def printPattern():
    print("")
    for i in range(40):
        print("* ", end="")
    print("\n")

testList = ['bengaluru', 'New York', 1971, 1682, (1, 2, 3, 4, 5, 'is this a tuple?'), "hello, welcome to python programming"]

# 6.1 :     try to extract the entire tuple by using positive indexing

print("PRINTING TUPLE BY USING +VE INDEXING : ")
print("i)",testList[4])

printPattern()

# 6.2 :     can we add elements into tuple after creating it?
# A   :     No

# 6.3 :     remove 1682 and 'New York' from the list
testList.remove(1682)
testList.remove('New York')

print("LIST AFTER REMOVING \n1 : 1682\n2 : 'New York'\n")
print(testList)

printPattern()

# 6.4 :     discuss one practical application of tuple and lists
# A   :     lists can be used to maintain dynamic records while tuples are used for storing immutable (something that can't be changed) data

# 6.5 :     access 'bengaluru' by negative indexing
print("ACCESSING 'bengaluru' BY NEGATIVE INDEXING : ")
print(testList[-4])

printPattern()

# 6.6 :     Add 'mumbai' into the list
print("ADDING 'mumbai' TO THE LIST : ")
testList.append('mumbai')
print(testList)

printPattern()

# 6.7 :     try to perform one operation on each removal operation on lists (?)
print(testList)

# using remove()
testList.remove('bengaluru')
print(testList)

# using del
del testList[3]
print(testList)

# using pop()
testList.pop(-1)    # removes 'mumbai' from the list
print(testList)

# =================== CONTINUED ========================

testList.append('chennai')
print(testList)

testList.extend('kolkata')
print(testList)

testList.insert(1, 'hyderabad')
print(testList)