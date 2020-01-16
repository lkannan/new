# initializing blockchain
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []

}
blockchain = [genesis_block]
open_transactions = []
owner = 'Kannan'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, amount=1.0, sender=owner):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:

        :sender: sender of the amount.
        :recipient: reciever of the amount.
        :amount: transaction amount (default = 1.0).
    """
    transcation = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transcation)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_user_input():
    """
    Returns the input of the user (new transaction amount) as a float.
    """
    tx_recipient = input("Enter the recipient: ")
    tx_amount = float(input("Enter transactional amount: "))
    return tx_recipient, tx_amount


def verify_chain():
    for block_index in range(1, len(blockchain)):
        if not blockchain[block_index][0] == blockchain[block_index-1]:
            return False
    return True


exit_condition = True

while exit_condition:
    print("Please choose")
    print("1. Add new transaction")
    print("2. Mine a new block")
    print("3. Print blockchain blocks")
    print('h. Edit blockchain')
    print("q. Quit")
    user_choice = input("Your choice: ")
    if user_choice == "1":
        tx_recipient, tx_amount = get_user_input()
        add_transaction(tx_recipient, tx_amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == "3":
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
    # if not verify_chain():
    #     print('Invalid blockchain')
    #     break
