import unittest
import lesson26_blockchain as l
import timeit


class BlockChainTest(unittest.TestCase):
    def test_hash(self):
        bl_ch = l.BlockChain('0')
        bl_ch.chain_block[0].data = 'Hi'
        self.assertNotEqual(bl_ch.hash(bl_ch.chain_block[0]), None)

    def test_choice_hash(self):
        bl_ch1 = l.BlockChain('0')
        bl_ch1.chain_block[0].data = 'Hi'

        bl_ch2 = l.BlockChain('00')
        bl_ch2.chain_block[0].data = 'Hi mag'

        bl_ch3 = l.BlockChain('000')
        bl_ch3.chain_block[0].data = 'Hi mag'

        self.assertEqual(bl_ch1.choice_hash(bl_ch1.chain_block[0])[-1], '0')
        self.assertTrue(bl_ch2.choice_hash(bl_ch2.chain_block[0]).endswith('00'))
        self.assertTrue(bl_ch3.choice_hash(bl_ch3.chain_block[0]).endswith('000'))

    def test_add(self):
        bl_ch = l.BlockChain('000')
        bl_ch.chain_block[0].data = 'Hi'
        bl_ch.add('Bye')
        self.assertTrue(len(bl_ch.chain_block), 2)
        self.assertEqual(bl_ch.chain_block[1].data, 'Bye')
        self.assertEqual(bl_ch.chain_block[1].index, 1)
        self.assertTrue(bl_ch.chain_block[1].nonce)
        self.assertTrue(bl_ch.chain_block[1].own_hash.endswith('000'))
        self.assertTrue(bl_ch.chain_block[1].prev_hash.endswith('000'))

    def test_find(self):
        bl_ch = l.BlockChain('000')
        bl_ch.chain_block[0].data = 'Hi'
        bl_ch.add('Bye')
        self.assertEqual(bl_ch.find('00000'), bl_ch.chain_block[0])
        # если time_creation = 15
        # self.assertEqual(bl_ch.find('f6bcbf0f5b91c65fe8152cfe4db5b000'), bl_ch.chain_block[1])

    def test_correction_block(self):
        bl_ch = l.BlockChain('000')
        bl_ch.chain_block[0].data = 'Hi'
        bl_ch.add('Bye')
        bl_ch.add('Hello!')
        bl_ch.add('Перевод на номер 123')
        # в строке ниже будет ошибка, которая говорит о правильности кода
        # bl_ch.chain_block[len(bl_ch.chain_block)-1].own_hash += '1'
        self.assertTrue(bl_ch.correction_block())

    @staticmethod
    def test_time():
        list_time = []
        for i in range(1, 7):
            print(i)
            start_time = timeit.default_timer()
            bl_ch = l.BlockChain('0' * i)
            bl_ch.chain_block[0].data = 'Hi'
            bl_ch.add('Bye')
            list_time.append((timeit.default_timer() - start_time, i))
        print(list_time)

if __name__ == '__main__':
    unittest.main()
