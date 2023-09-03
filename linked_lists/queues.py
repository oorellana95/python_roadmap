from collections import deque
from heapq import heappop, heappush
from itertools import count


class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()


class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


class PriorityQueueMinHeap(IterableMixin):
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)


class PriorityQueueMaxHeap(IterableMixin):
    """
    Implementation example:

    CRITICAL = 3
    IMPORTANT = 2
    NEUTRAL = 1

    messages = PriorityQueue()
    messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
    messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
    messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
    messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

    messages.dequeue()
    # 'Brake pedal depressed'
    """
    def __init__(self):
        self._elements = []
        self._counter = count()  # we could avoid creating the _counter if we add a timestamp below.

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (-priority, value))

    def dequeue(self):
        return heappop(self._elements)[-1]
