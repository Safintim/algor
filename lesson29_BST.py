from random import randint


class BST:
    def __init__(self, h):
        self.tree = [None] * (pow(2, h+1) - 1)

    @staticmethod
    def halve_arr(arr):
        halves_arr = [arr]

        for half in halves_arr:
            if half[:len(half) // 2]:
                halves_arr.append(half[:len(half) // 2])
                halves_arr.append(half[len(half) // 2 + 1:])
        return halves_arr

    def add(self, arr):
        arr.sort()
        halves_arr = self.halve_arr(arr)
        for i in range(len(self.tree)):
            if len(halves_arr[i]) // 2:
                self.tree[i] = halves_arr[i][len(halves_arr[i]) // 2]
            else:
                self.tree[i] = halves_arr[i][0]


# h = 2
# b = BST(h=h)
# test_list = [randint(1, 2**(h+2)) for _ in range(pow(2, h+1) - 1)]
# print(test_list)
# b.add(test_list)
#
# print('self.tree', b.tree, sep='-')
