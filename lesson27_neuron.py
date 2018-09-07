import os


class Neuron:
    def __init__(self, n, m):
        self.threshold = 35
        self.synapses = [[0] * n for i in range(m)]

    @staticmethod
    def read_file(file):
        list_line = []

        # читаем данные из файла
        with open(file, 'r') as f:
            for line in f:
                list_line.append([int(char) for char in line.strip()])
        return list_line

    @staticmethod
    def correct_wt(arr_wt, arr_in, flag):
        for i in range(0, len(arr_wt)):
            for j in range(0, len(arr_wt[i])):
                if flag:
                    arr_wt[i][j] += arr_in[i][j]
                else:
                    arr_wt[i][j] -= arr_in[i][j]
        return arr_wt

    def activation(self, list_line):
        total = 0

        # умножаем на соотв вес и суммируем
        for i in range(0, len(self.synapses)):
            for j in range(0, len(self.synapses[i])):
                total += list_line[i][j] * self.synapses[i][j]

        # да или нет
        if self.threshold > total:
            return 0
        else:
            return 1

    def learning(self, dir_name):
        list_dir = os.listdir(dir_name)
        done = 0
        count = 0

        # пока не распознал все файлы
        while done != len(list_dir) or count == 10**6:
            print(count)
            for i in list_dir:
                # читаем файл и преобразуем в удобный вид для вычислений
                list_line = self.read_file(dir_name + '/' + i)
                # распознавание
                temp = self.activation(list_line)

                # если это буква отличная от А, но распоз как А
                if temp == int(i[2]) and 'A' != i[0]:
                    self.correct_wt(self.synapses, list_line, True)
                # если это А, но неправильно распоз
                elif temp != int(i[2]) and 'A' == i[0]:
                    self.correct_wt(self.synapses, list_line, False)
                # если все четко
                elif temp == int(i[2]) and 'A' == i[0]:
                    done += 1
            count += 1

        return done, count

# n = Neuron(10,10)
# print(n.synapses)
# print(n.activation('lesson27/A_+_1'))