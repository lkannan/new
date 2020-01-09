# initializing blockchain
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transactional_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:

        :transactional amount: The amount that should be added.
        :last transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transactional_amount])


def get_user_input():
    """
    Returns the input of the user (new transaction amount) as a float.
    """
    return float(input("Enter transactional amount: "))


def verify_chain():
    for block_index in range(1, len(blockchain)):
        if not blockchain[block_index][0] == blockchain[block_index-1]:
            return False
    return True


exit_condition = True

while exit_condition:
    print("Please choose")
    print("1. Add new transaction")
    print("2. Print blockchain blocks")
    print('h. Edit blockchain')
    print("q. Quit")
    user_choice = input("Your choice: ")
    if user_choice == "1":
        add_value(get_user_input(), get_last_blockchain_value())
    elif user_choice == "2":
        for block in blockchain:
            print(block)
        else:
            print('_' * 20)
    elif user_choice == 'h':
        if len(blockchain) > 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        exit_condition = False
    else:
        print("Input was invalid")
    if not verify_chain():
        print('Invalid blockchain')
        break
