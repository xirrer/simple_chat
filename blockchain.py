import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Устанавливаем сложность майнинга

    def create_genesis_block(self):
        return Block(0, time.time(), 'Genesis Block', '0')

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        if new_block.index == self.get_latest_block().index + 1 and \
                new_block.previous_hash == self.get_latest_block().hash:
            new_block.mine_block(self.difficulty)
            self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Пример использования

# Создание блокчейна
my_blockchain = Blockchain()

# Добавление блоков
block1 = Block(1, time.time(), 'Data 1', my_blockchain.get_latest_block().hash)
my_blockchain.add_block(block1)

block2 = Block(2, time.time(), 'Data 2', my_blockchain.get_latest_block().hash)
my_blockchain.add_block(block2)

# Вывод информации о блокчейне
while True:
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print()
        time.sleep(5)