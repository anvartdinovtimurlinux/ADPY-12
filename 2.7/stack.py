class Stack:
    def __init__(self):
        self._storage = []

    def is_empty(self):
        return bool(self._storage)

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        return self._storage.pop()

    def peek(self):
        return self._storage[-1]

    def size(self):
        return len(self._storage)
