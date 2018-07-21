import unittest
import lesson7_deque as l


class DequeTest(unittest.TestCase):

    def test_palindrom(self):
        test_list = ['довод', 'заказ', 'радар', 'banan', 'apple', 'lsdkjfskf']
        result = [True, True, True, False, False, False]
        result_func = (l.palindrom(i) for i in test_list)

        self.assertListEqual(result, list(result_func))


if __name__ == '__main__':
    unittest.main()
