def SelectionSortStep(array, i=0):
    if i < 0:
        return array
    for i in range(i, len(array)):
        index_min = i
        for j in range(i+1, len(array)):
            if array[index_min] > array[j]:
                index_min = j
        array[i], array[index_min] = array[index_min], array[i]


def BubbleSortStep(array):

    is_not_sorted = True
    while is_not_sorted:
        is_not_sorted = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_not_sorted = True

    return True


def sort_insert(n, step):
    for i in range(step, len(n)):
        x = n[i]
        j = i - step
        while (j > -1) & (n[j] > x):
            n[j+step] = n[j]
            j -= step
        n[j+step] = x
    return n


def sort_shell(n):

    step = 1
    for i in range(len(n) // 3):
        step = 3 * step + 1

    while step > 0:

        for i in range(step, len(n)):
            x = n[i]
            j = i - step
            while (j > -1) & (n[j] > x):
                n[j+step] = n[j]
                j -= step
            n[j+step] = x
        step //= 3
    return n
