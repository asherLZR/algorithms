from Algorithms.abstract_data_types.referential_array import build_array


class Heap:

    def __init__(self):
        self.array = build_array(100)
        self.count = 0

    def __len__(self):
        return self.count

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def largest_child(self, k):
        # if the last element in the heap is the left child, then there is no right
        # or if the the left child is greater than the right, return index for left
        if 2 * k == self.count or self.array[2*k][0] > self.array[2*k+1][0]:
            return 2*k
        else:
            return 2*k+1

    def rise(self, k):
        while k > 1 and self.array[k//2][0] < self.array[k][0]:
            self.swap(k, k//2)
            k //= 2

    def sink(self, k):
        # 2k and 2k+1
        while 2 * k <= self.count:
            child = self.largest_child(k)
            if self.array[k][0] >= self.array[child][0]:
                break
            self.swap(child, k)
            k = child

    def get_max(self):
        if len(self) == 0:
            raise ValueError("There is no max in an empty heap!")
        item = self.array[1]
        self.swap(1, self.count)
        self.count -= 1
        self.sink(1)
        return item[1]

    def add(self, key, value):
        item = (key, value)
        if self.count + 1 < len(self.array):
            self.array[self.count+1] = item
        else:
            self._resize()
            self.array[self.count+1] = item
        self.count += 1
        self.rise(self.count)

    def _resize(self):
        new_array = build_array(2*len(self.array))
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array


def heap_sort(a_list):
    my_heap = Heap()
    for elem in a_list:
        my_heap.add(elem, elem)
    for i in range(len(my_heap)-1, -1, -1):
        a_list[i] = my_heap.get_max()
    return a_list


def main():
    pass


if __name__ == '__main__':
    main()
