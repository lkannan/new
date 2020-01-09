# initializing blockchain 
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]


def add_value(transactional_amount, last_transaction=[1]):
    ''' Append a new value as well as the last blockchain value to the blockchain

    Arguments:

        :transactional amount: The amount that should be added.
        :last transaction: The last blockchain transaction (default [1]).
    '''
    blockchain.append([last_transaction, transactional_amount])


def get_user_input():
    '''
    Returns the input of the user (new transaction amount) as a float.
    '''
    return (float(input('Enter transactional amount: ')))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(get_last_blockchain_value())
