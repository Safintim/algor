from lesson10_ass_arr import NativeDictionary


class NativeCache(NativeDictionary):
    def __init__(self, sz):
        NativeDictionary.__init__(self, sz)
        self.hits = [0] * self.size

    def put(self, key, value):
        index = self.find(key)
        if index is not None:
            if self.slots[index] == key:
                self.values[index] = value
                self.hits[index] += 1
                return True

        index = self.seek_slot(key)
        if index is None:
            old = self.hits.index(min(self.hits))
            self.slots[old] = key
            self.values[old] = value
            self.hits[old] = 1
        else:
            self.slots[index] = key
            self.values[index] = value
            self.hits[index] += 1
        return True

    def get(self, key):
        key = self.find(key)
        if key is None:
            return None
        else:
            self.hits[key] += 1
            return self.values[key]
