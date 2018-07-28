from abstract_data_types.referential_array import build_array


class ArrayList:
    def __init__(self, max_capacity):
        assert max_capacity > 0, "Cannot build an empty list"
        self.count = 0
        self.array = build_array(max_capacity)

    def __len__(self):
        return self.count

    def __str__(self):
        if self.count == 0:
            return "[]"
        my_string = "["
        for i in range(len(self)):
            my_string += str(self.array[i]) + ", "
        my_string = my_string[:-2]
        my_string += "]"
        return my_string

    def __iter__(self):
        return ListIterator(self)

    def is_full(self):
        return self.count >= len(self.array)

    def is_empty(self):
        return self.count == 0

    def append(self, item):
        assert not self.is_full(), "Cannot append to a full array"
        self.array[self.count] = item
        self.count += 1


class ListIterator:
    def __init__(self, array_list):
        self.array = array_list.array
        self.count = array_list.count
        self.last = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.last >= self.count:
            raise StopIteration("No more elements to iterate through")
        self.last += 1
        return self.array[self.last-1]


a_list = ArrayList(1000)
a_list.append("Hello")
a_list.append("World")
print(a_list)
my_iter = iter(a_list)
print(next(my_iter))
print(next(my_iter))