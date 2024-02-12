from queue import Queue

myQueue = Queue(maxsize= 10)    # declared queue of size 10

myQueue.put(21)
myQueue.put(23)
myQueue.put(10)
myQueue.put(50)
myQueue.put(90)

i1 = myQueue.get()
i2 = myQueue.get()

print(i1, i2)