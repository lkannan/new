blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transactional_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transactional_amount])


tx_amount = float(input('Enter transactional amount: '))
add_value(tx_amount)

tx_amount = float(input('Enter transactional amount: '))
add_value(tx_amount, get_last_blockchain_value())

tx_amount = float(input('Enter transactional amount: '))
add_value(tx_amount, get_last_blockchain_value())

print(get_last_blockchain_value())
