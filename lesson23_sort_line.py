
def hash_fun(value, words):
    first = value[0]
    last = int(value[1:])
    return last + 100 * words.index(first)


# AMN A - abcdefgh, MN - 0-9 = 800

def ksort(n, d):
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    a = [[] for i in range(d)]
    result = []

    for i in n:
        h = hash_fun(i, words)
        a[h].append(i)
    for i in a:
        if len(i) != 0:
            for j in i:
                result.append(j)
    return result


