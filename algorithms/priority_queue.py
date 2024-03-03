from queue import PriorityQueue

# Create a priority queue
my_priority_queue = PriorityQueue()

# Enqueue elements with priorities
my_priority_queue.put((2, "Task 1"))
my_priority_queue.put((1, "Task 2"))
my_priority_queue.put((3, "Task 3"))

# Dequeue elements based on priority
task1 = my_priority_queue.get()
task2 = my_priority_queue.get()
task3 = my_priority_queue.get()

print("Dequeued tasks:", task1, task2, task3)
