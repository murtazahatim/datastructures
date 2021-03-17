class HashtableLinearProbing:
    def __init__(self, size=5):
        self.count = 0
        self.tablesize = size
        self.array = [None] * self.tablesize

    def hash(self, key):
        if type(key) == str:
            value = 0
            base = 31
            for char in key:
                value = ((value * base) + ord(char)) % self.tablesize
            return value
        else:
            return int(key) % self.tablesize

    def linear_probe_set(self, key, value):
        position = self.hash(key)
        for _ in range(self.tablesize):
            if self.array[position] is None:
                self.array[position] = (key, value)
                self.count += 1
                return
            elif self.array[position][0] == key:
                self.array[position] = (key, value)
                return
            else:
                position = (position + 1) % self.tablesize
        if self.count / self.tablesize > 0.5:
            self.rehash()
        self.linear_probe_set(key, value)

    def linear_probe_get(self, key):
        position = self.hash(key)
        for _ in range(self.tablesize):
            if self.array[position] is None:
                raise KeyError
            elif self.array[position][0] == key:
                return self.array[position][1]
            else:
                position = (position + 1) % self.tablesize

    def linear_probe_del(self, key):
        position = self.hash(key)
        for _ in range(self.tablesize):
            if self.array[position] is None:
                raise KeyError
            elif self.array[position][0] == key:
                self.array[position] = None
                self.count -= 1
                break
            else:
                position = (position + 1) % self.tablesize
        position += 1
        while self.array[position] is not None:
            self.linear_probe_set(self.array[position][0], self.array[position][1])

    def rehash(self):
        self.tablesize = 1 + (self.tablesize * 2)
        old_array = self.array
        self.array = [None] * self.tablesize

        for entry in old_array:
            if entry is not None:
                self.linear_probe_set(entry[0], entry[1])