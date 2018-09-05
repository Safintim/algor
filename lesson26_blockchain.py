import hashlib
import random as ran
from datetime import datetime


class Block:
    def __init__(self, data=None, prev_hash=None, index=None):
        self.data = data
        self.prev_hash = prev_hash
        self.index = index + 1
        self.time_creation = datetime.now()
        # для теста
        # self.time_creation = 15
        self.own_hash = None
        self.nonce = None


class BlockChain:
    def __init__(self, count_zero):
        self.chain_block = [Block(prev_hash='00000', index=-1)]
        self.chain_block[0].own_hash = '00000'
        self.count_zero = count_zero

    @staticmethod
    def hash(block):
        result_hash = hashlib.md5(block.prev_hash.encode())
        result_hash.update(str(block.data).encode())
        result_hash.update(str(block.index).encode())
        result_hash.update(str(block.time_creation).encode())
        if block.nonce:
            result_hash.update(str(block.nonce).encode())

        return result_hash.hexdigest()

    def choice_hash(self, block):
        r = self.hash(block)
        if not block.nonce:
            block.nonce = 0
        while not r.endswith(self.count_zero):
            block.nonce += 1
            r = self.hash(block)
        return r

    def add(self, data):
        last_block = self.chain_block[len(self.chain_block) - 1]
        block = Block(data=data, prev_hash=last_block.own_hash, index=last_block.index)
        block.own_hash = self.choice_hash(block)
        self.chain_block.append(block)

    def find(self, block_hash):
        for block in self.chain_block:
            if block.own_hash == block_hash:
                return block

    def correction_block(self):
        for block in self.chain_block:
            if not block.own_hash.endswith(self.count_zero):
                print('Ошибка', block.index)
                return False
        print('ОК')
        return True


# bl_chain = BlockChain('000')
# bl_chain.add('Hi')

# for i in bl_chain.chain_block:
#     print(i.data, i.index, i.prev_hash, i.own_hash)
