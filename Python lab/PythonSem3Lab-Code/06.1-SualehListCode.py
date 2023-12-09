l=[]
l.append("Bengaluru")
l.append("New York")
l.append(1971)
l.append("1682")
l.append((1,2,3,4,5,'is this tuple?'))
l.append("Hello, Welcome to Python Programming")
print(l)
print("(i)",l[4])
l.remove('1682')
l.remove('New York')
print("(iii)",l)
print("(v)",l[-4])
l.append("Mumbai")
print("(vi)",l)
l=['Bengaluru', 'New York', 1971, '1682', (1, 2, 3, 4, 5, 'is this tuple?'), 'Hello, Welcome to Python Programming','Mumbai']
#deletion methods:
#1.using remove
l.remove("Bengaluru")
print("New List:",l)
#2.using del
del l[2]
print("New List:",l)
#3.using list comprehension
new_list=[i for i in l if i!='Mumbai']
print("New List:",new_list)
#4. using pop()
l.pop(4)
print("New List:",l)
#5. using discard()
l=set(l)
l.discard('New York')
print("New List:",l)
print(" ")
print(l)
#6. using filter()
l=filter(lambda item:item!=(1, 2, 3, 4, 5, 'is this tuple?'),l)
print(list(l))
#7. using last slicing
l=['Bengaluru', 'New York', 1971, '1682', (1, 2, 3, 4, 5, 'is this tuple?'), 'Hello, Welcome to Python Programming','Mumbai']
l=l[:3]+l[4:]
print(l)