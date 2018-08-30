def find_start_end(flag, result, i):
    """
    Находит начало и конец аргументов
    """
    brackets = 1
    if flag:
        j = i + 2
        while brackets != 0:
            if result[j] == '(':
                brackets += 1
            elif result[j] == ')':
                brackets -= 1
            j += 1
    else:
        j = i - 2
        while brackets != 0:
            if result[j] == '(':
                brackets -= 1
            elif result[j] == ')':
                brackets += 1
            j -= 1

    return j


def add_brackets(operator, s):
    result = s.split()
    i = 0
    while i <= len(result) - 1:
        if result[i] == operator:
            if i + 2 <= len(result) - 1:  # чтобы избежать IndexError

                if result[i - 1] == ')':  # если перед стоит закр скобка, то нужно найти начало аргумента
                    j = find_start_end(False, result, i)
                    result.insert(j + 1, '(')
                    i += 1
                elif result[i - 2] != '(':  # если нет скобочек, то поставить скобочку
                    result.insert(i - 1, '(')
                    i += 1

                if result[i+1] == '(':  # если после стоит откр скобка, то нужно найти конец аргумента
                    j = find_start_end(True, result, i)
                    result.insert(j, ')')
                    i += 1
                elif result[i+2] != ')':  # если нет, то поставить
                    result.insert(i+2, ')')
                    i += 1

            else:  # если сюда попали, значит, это конец строки и в конце нет скобки
                result.insert(i + 2, ')')

                if result[i - 1] != ')':
                    result.insert(i - 1, '(')
                if result[i - 1] == ')':
                    j = find_start_end(False, result, i)
                    result.insert(j + 1, '(')
                    i += 1

        i += 1
    return ' '. join(result)


i1 = add_brackets('/', '7 + 3 / 25 * ( 5 - 2 ) ')
print(i1)
i2 = add_brackets('*', i1)
print(i2)
i3 = add_brackets('-', i2)
print(i3)
i4 = add_brackets('+', i3)
print(i4)