from collections import deque


class Queue:  # FIFO
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()

    def first(self):
        return self.queue[-1]

    def size(self) -> int:
        return len(self.queue)

    def isEmpty(self) -> bool:
        return self.size() == 0

    def printQueue(self):
        print(self.queue)

if __name__ == "__main__":
    newQueue = Queue()
    newQueue.enqueue(5)
    newQueue.enqueue(50)
    newQueue.enqueue(500)
    newQueue.printQueue()
    print(newQueue.size())
    print(newQueue.dequeue())
    print(newQueue.dequeue())
    print(newQueue.dequeue())

    print(newQueue.size())

    print(newQueue.isEmpty())