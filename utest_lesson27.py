import unittest
import lesson27_neuron as l
import os


class MyTestCase(unittest.TestCase):
    def test_activation(self):
        n = l.Neuron(10, 10)
        result_list = []
        list_dir = os.listdir('lesson27')
        for i in list_dir:
            result_list.append(n.activation('lesson27/' + i))

        self.assertListEqual(result_list, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
