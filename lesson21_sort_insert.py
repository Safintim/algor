

# [7,6,5,4,3,2,1]
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
