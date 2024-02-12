# declare queue as a list
queue = []

# append values to the queue (enqueue-ing)
queue.append(21)
queue.append(23)
queue.append(10)
queue.append(50)
queue.append(90)

# print the queue
print(queue)            # [21, 23, 10, 50, 90]

# pop the first element of the queue (dequeue-ing)
queue.pop(0)            # removes 21 from queue

# print the dequeued elements
print(queue.pop(0))     # prints 23 - removed from queue
print(queue.pop(0))     # prints 10 - removed from queue

# print the final queue
print(queue)            # [50, 90]