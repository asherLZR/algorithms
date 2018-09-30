import heapq, json

class PriorityQueue:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)

    def add(self, priority, item):
        heapq.heappush(self.array, (-1 * priority, item))

    def pop(self):
        if self.__len__() == 0:
            raise EmptyQueueError("The queue is empty!")
        return heapq.heappop(self.array)

    def peek(self):
        if self.__len__() == 0:
            raise EmptyQueueError("The queue is empty!")
        return self.array[0]

class EmptyQueueError(Exception):
    pass

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.add(1, "a")
    pq.add(10, "b")
    pq.add(100, "c")
    b = map(lambda tup: ": ".join(tuple(map(str, tup))), pq.array)
    json_str = "{"
    for x in b:
        json_str += x + ", "
    json_str = json_str[:-2]
    json_str += "}"
    print(json_str)
