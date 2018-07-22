from lesson10_ass_arr import HashTable


class Cache(HashTable):
    def __init__(self, sz, stp):
        HashTable.__init__(self, sz, stp)
        self.count_call = [0] * self.size

    def put(self, key, value):
        index = self.find(key)
        if index is not None:
            if self.slots[index] == key:
                self.values[index] = value
                self.count_call[index] += 1
                return True

        index = self.seek_slot(key)
        if index is None:
            old = self.count_call.index(min(self.count_call))
            self.slots[old] = key
            self.values[old] = value
            self.count_call[old] = 1
            return True
        else:
            self.slots[index] = key
            self.values[index] = value
            self.count_call[index] += 1
            return True

    def get(self, key):
        key = self.find(key)
        if key is None:
            return None
        else:
            self.count_call[key] += 1
            return self.values[key]
