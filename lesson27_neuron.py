class Neuron:
    def __init__(self, n, m):
        self.threshold = 35
        self.synapses = [[0] * n for i in range(m)]

    def activation(self, file):
        list_line = []
        total = 0

        # читаем данные из файла
        with open(file, 'r') as f:
            for line in f:
                list_line.append([int(char) for char in line.strip()])

        # умножаем на соотв вес и суммируем
        for i in range(0, len(self.synapses)):
            for j in range(0, len(self.synapses[i])):
                total += list_line[i][j] * self.synapses[i][j]

        # да или нет
        if self.threshold > total:
            return 0
        else:
            return 1

# n = Neuron(10,10)
# print(n.synapses)
# print(n.activation('lesson27/A_+_1'))