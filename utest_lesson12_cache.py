import unittest
import lesson12_cache as l


class CacheTest(unittest.TestCase):

    @staticmethod
    def create_dict():
        test_list = [3, 93, 60, 25, 73, 83, 45, 29, 18, 8, 28, 48, 40, 88, 0, 32, 15]
        c = l.NativeCache(17)

        for i in range(97, 114):
            c[chr(i)] = test_list[i - 97]

        return c

    def test_put_get(self):
        c = self.create_dict()
        print(c.slots)
        print(c.values)
        print(c.hits)
        k = 0
        while k < 2:
            for i in range(97, 113):
                c[chr(i)]
            k += 1
        c[chr(113)]
        # в итоге получаем
        # [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3]
        # теперь добавим новый слот в кэш. и обратимся к нему 4 раза
        for i in range(4):
            c['zx'] = 10 * i
        # и еще один слойт
        c['zzz'] = 999

        index_zx = c.slots.index('zx')
        index_zzz = c.slots.index('zzz')

        self.assertTrue(c.is_key('zx'))
        self.assertTrue(c.is_key('zzz'))
        self.assertTrue(c.hits[index_zzz], 1)
        self.assertEqual(c.hits[index_zx], 4)


if __name__ == '__main__':
    unittest.main()
