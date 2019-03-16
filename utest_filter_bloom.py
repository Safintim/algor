import unittest
import filter_bloom as t


class MyTestCase(unittest.TestCase):
    def test_data(self):
        source_str = '0123456789'

        test_strings = [source_str]
        for i in range(9):
            source_str = source_str[1:] + source_str[0]
            test_strings.append(source_str)

        return test_strings

    def test_print_test_data(self):
        print(self.test_data())

    def test_hash1(self):
        test_strings = self.test_data()
        filter = t.BloomFilter()

        for str in test_strings:
            print(filter.hash1(str))

    def test_hash2(self):
        test_strings = self.test_data()
        filter = t.BloomFilter()

        for str in test_strings:
            print(filter.hash2(str))

    def test_add(self):
        test_strings = self.test_data()
        filter = t.BloomFilter()

        for str in test_strings:
            filter.add(str)

        print(filter.filter)

    def test_is_value(self):
        test_strings = self.test_data()
        filter = t.BloomFilter()

        for str in test_strings:
            filter.add(str)

        for str in test_strings:
            self.assertTrue(filter.is_value(str))

if __name__ == '__main__':
    unittest.main()
