import string

# Find all of the numbers from 1-1000 that are divisible by 7
numbers = list(range(1000))
print([x for x in numbers if x % 7 == 0])
""" however this is very simple and can be done without
list comprehension, just by using range function """
print(list(range(0, 1000, 7)))


# Find all of the numbers from 1-1000 that have a 3 in them
print([x for x in numbers if "3" in str(x)])


# list comprehension with if-else
""" square only the even numbers between 1-100 and
 return squared even and original odd num """
print([x ** 2 if x % 2 == 0 else x for x in numbers[:100]])


# multi dimensional comprehension
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print([x for row in mat for x in row])


# Count the number of spaces in a string
sentence = "Count the number of spaces in a string"
print(len([x for x in sentence if x == " "]))


# Remove all of the vowels in a string
vowels = "AaEeIiOoUu"
print("".join([x for x in sentence if x not in vowels]))


# Find all of the words in a string that are less than 4 letters
print([x for x in sentence.split() if len(x) < 4])


""" Use a dictionary comprehension to count
 the length of each word in a sentence. """
print({word: len(word) for word in sentence.split()})


""" Use a nested list comprehension to find all of the numbers
    from 1-1000 that are divisible by any single digit besides 1 (2-9) """
divisors = list(range(2, 10))
print(list(set([x for x in numbers for y in divisors if x % y == 0])))


"""two lists accessing in list comprehension"""
mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
print([(i, mylist[i], mylist.index(i)) for i in list_b])
# dictionary comprehension
print({i: mylist.index(i) for i in list_b})


sentences = [
    "a new world record was set",
    "in the holy city of ayodhya",
    "on the eve of diwali on tuesday",
    "with over three lakh diya or earthen lamps",
    "lit up simultaneously on the banks of the sarayu river",
]
stopwords = ["for", "a", "of", "the", "and", "to", "in", "on", "with"]
print(
    [
        word
        for sentence in sentences
        for word in sentence.split()
        if word not in stopwords
    ]
)
# to keep the list of sentences intact
print(
    [
        [word for word in sentence.split() if word not in stopwords]
        for sentence in sentences
    ]
)
# joining the words
print(
    [
        " ".join([word for word in sentence.split() if word not in stopwords])
        for sentence in sentences
    ]
)


""" Question 1. Given a 1D list, negate all elements which
 are between 3 and 8, using list comprehensions
 """
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x * -1 if x >= 3 and x <= 8 else x for x in mylist])
print([-i if 3 <= i <= 8 else i for i in mylist])


# 2: Make a dictionary of the 26 english alphabets
#  mapping each with the corresponding integer.
alphabets = string.ascii_lowercase
{key: alphabets.index(key) + 1 for key in string.ascii_lowercase}
alpha = {key: value for key, value in zip(string.ascii_lowercase, range(1, 27))}


""" 3: Replace all alphabets in the string ‘Lee Quan Yew’, by substituting
the alphabet with the corresponding numbers. """
sentence = "Lee Quan Yew".lower()
[alpha[x] if x != " " else " " for x in sentence]
# another way by using dict.get function,
# it is helpful to avoid missing values in dict
[alpha.get(x, " ") for x in sentence]


# 4: Get the unique list of words from the
# following sentences, excluding any stopwords.
sentences = [
    "The Hubble Space telescope has spotted",
    "a formation of galaxies that resembles",
    "a smiling face in the sky",
]
set(
    [
        word
        for sentence in sentences
        for word in sentence.split()
        if word not in stopwords
    ]
)


# 5: Tokenize the following sentences excluding all stopwords and punctuations.
sentences = [
    "The Hubble Space telescope has spotted",
    "a formation of galaxies that resembles",
    "a smiling face in the sky",
    "The image taken with the Wide Field Camera",
    "shows a patch of space filled with galaxies",
    "of all shapes, colours and sizes",
]

stopwords = ["for", "a", "of", "the", "and", "to", "in", "on", "with"]
[
    [word.lower() for word in sentence.split() if word not in stopwords]
    for sentence in sentences
]


# 6: Create a list of (word:id) pairs for all
# words in the following sentences, where id is the sentence index.
[
    (word, sentences.index(sentence))
    for sentence in sentences
    for word in sentence.split()
]
# another approach using enumerate
[
    (word, i)
    for i, sentence in enumerate(sentences)
    for word in sentence.split()
]


# 7: Print the inner positions of the 64 squares
# in a chess board, replacing the boundary squares with the string ‘—-‘.
chess_board = [[(i,j) if(i not in (0,7) and j not in (0,7)) else '—-' for i in range(8)] for j in range(8)]
for row in chess_board:
    print(row)

[print(row) for row in chess_board]

""" For all the numbers 1-1000, use a nested list/dictionary comprehension
 to find the highest single digit any of the numbers is divisible by """
