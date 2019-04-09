#!/usr/bin/python3
"""Множества. код основан на lesson9_hash.py"""


class PowerSet:
    def __init__(self):
        self.set = []

    def size(self):
        return len(self.set)

    def put(self, value):
        if value not in self.set:
            self.set.append(value)

    def remove(self, value):
        if value in self.set:
            self.set.remove(value)
            return True
        return False

    def get(self, value):
        if value in self.set:
            return True
        return False

    def intersection(self, powset):
        temp = PowerSet()

        for item in self.set:
            if item in powset.set:
                temp.put(item)

        for item in powset.set:
            if item in self.set:
                temp.put(item)

        return temp

    def union(self, powset):
        if powset.set:
            temp = PowerSet()
            for item in self.set:
                temp.put(item)
            for item in powset.set:
                temp.put(item)

            return temp
        return self

    def difference(self, powset):
        temp = []
        for item in self.set:
            if item not in powset.set:
                temp.append(item)

        # self.set = temp
        return temp

    def issubset(self, powset):
        for item in self.set:
            if item not in powset.set:
                return False
        return True
