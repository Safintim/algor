def SelectionSortStep(array, i=0):
    if i < 0:
        return array
    index_min = i
    for k in range(i+1, len(array)):
        if array[index_min] > array[k]:
            index_min = k
    array[i], array[index_min] = array[index_min], array[i]


def BubbleSortStep(array):
    is_sorted = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            is_sorted = False
    return is_sorted


def InsertionSortStep(array, step, i):
    if step < 1 and i < 0:
        return array

    for i in range(i+step, len(array), step):
        current = array[i]
        index = i

        while index >= step and array[index-step] > current:
            array[index] = array[index-step]
            index -= step
        array[index] = current


def KnuthSequence(len_array):
    step = 1
    knuth_sequence = [step]
    while 3 * step + 1 < len_array:
        step = 3 * step + 1
        knuth_sequence.append(step)

    return knuth_sequence[::-1]

print(KnuthSequence(15))
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
