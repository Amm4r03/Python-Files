import queue
q1 = queue.Queue()
q1.put(10)
item1 = q1.get()
print("the item removed from the queue is {}".format(item1))