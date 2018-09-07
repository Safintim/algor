import unittest
import lesson27_neuron as l
import os


class MyTestCase(unittest.TestCase):
    def test_read_file(self):
        n = l.Neuron(10, 10)
        list_dir = os.listdir('lesson27')
        b_0 = n.read_file('lesson27/' + list_dir[0])
        result_str = ''
        for i in b_0:
            result_str += ''.join(str(item) for item in i) + '\n'
        f = open('lesson27/' + list_dir[0], 'r')
        self.assertTrue(result_str, f.read())
        f.close()

    def test_correct_wt(self):
        n = l.Neuron(10, 10)
        arr_wt = [[1, 1] * 2 for i in range(3)]
        arr_in = [[1, 1] * 2 for i in range(3)]
        self.assertListEqual(n.correct_wt(arr_wt, arr_in, False), [[0, 0] * 2 for i in range(3)])
        self.assertListEqual(n.correct_wt(arr_wt, arr_in, False), [[-1, -1] * 2 for i in range(3)])
        self.assertListEqual(n.correct_wt(arr_wt, arr_in, True), [[0, 0] * 2 for i in range(3)])

    def test_activation(self):
        n = l.Neuron(10, 10)
        result_list = []
        list_dir = os.listdir('lesson27')
        for i in list_dir:
            list_line = n.read_file('lesson27/' + i)
            result_list.append(n.activation(list_line))
        self.assertListEqual(result_list, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_learning(self):
        n = l.Neuron(10, 10)
        result = n.learning('lesson27/')
        self.assertEqual(result[0], 10)
        print(result)



if __name__ == '__main__':
    unittest.main()
