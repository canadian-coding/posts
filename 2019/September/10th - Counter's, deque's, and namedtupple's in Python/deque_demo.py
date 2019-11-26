from collections import deque

my_queue = deque(["james","john","tommy","emilia","Candace"])

# The pop() method removes items from the queue and returns them
print(f"{my_queue.pop()} has been removed from queue")

for line_location in range(len(my_queue)):
    """Because my_queue.pop() is called in the iteration, the
    deque object ends up being empty"""
    print(f"{my_queue.pop()} was in position {line_location + 1}")

print(f"Queue is empty: {my_queue}") # will be empty now

# .append() appends iterable/object to rightmost of the queue
my_queue.append("joanna") 

# Be careful, this appends the list to the queue, not each item
my_queue.append(["julia", "frank"]) 

# Appends an iterable/object to the leftmost of the queue
my_queue.appendleft("david")

print(f"Current Queue: {my_queue} <-- Notice Julia and Frank are together")
