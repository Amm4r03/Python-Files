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

testList = ['bengaluru', 'New York', 1971, 1682, 1, 2, 3, 4, 5, 'is this a tuple?', "hello, welcome to python programming"]

# 6.1 :     try to extract the entire tuple by using positive indexing

print("PRINTING LIST BY USING +VE INDEXING : ")
for i in testList:
    print(i)

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
# A   :     

# 6.5 :     access 'bengaluru' by negative indexing
print("ACCESSING 'bengaluru' BY NEGATIVE INDEXING : ")
print(testList[-9])

printPattern()

# 6.6 :     Add 'mumbai' into the list
print("ADDING 'mumbai' TO THE LIST : ")
testList.append('mumbai')
print(testList)

printPattern

# 6.7 :     try to perform one operation on each removal operation on lists (?)