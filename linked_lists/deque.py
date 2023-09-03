from collections import deque

deque(['a', 'b', 'c'])
# deque(['a', 'b', 'c'])

deque('abc')
# deque(['a', 'b', 'c'])

deque([{'data': 'a'}, {'data': 'b'}])
# deque([{'data': 'a'}, {'data': 'b'}])


llist = deque("abcde")
# deque(['a', 'b', 'c', 'd', 'e'])

llist.append("f")
# deque(['a', 'b', 'c', 'd', 'e', 'f'])

llist.pop()
# 'f'
# deque(['a', 'b', 'c', 'd', 'e'])

llist.appendleft("z")
# deque(['z', 'a', 'b', 'c', 'd', 'e'])

llist.popleft()
# 'z'
# deque(['a', 'b', 'c', 'd', 'e'])


def queue_implementation_example():
    """You want to add values to a list (enqueue), and when the timing is right, you want to remove the element that
    has been on the list the longest (dequeue). FIFO queues"""
    queue = deque()
    queue.append("Mary")
    queue.append("John")
    queue.append("Susan")
    print(queue.popleft())
    print(queue.popleft())


def stack_implementation_example():
    """You want to add values to a list (enqueue), and when the timing is right, you want to remove the element that
    has been on the list the longest (dequeue). FIFO queues"""
    history = deque()
    history.appendleft("https://realpython.com/")
    history.appendleft("https://realpython.com/pandas-read-write-files/")
    history.appendleft("https://realpython.com/python-csv/")
    print(history.popleft())
    print(history.popleft())
