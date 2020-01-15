# Find all of the numbers from 1-1000 that are divisible by 7
numbers = list(range(1000))
print([x for x in numbers if x % 7 == 0])
#however this is very simple and can be done without list comprehension, just by using range function
print(list(range(0, 1000, 7)))


# Find all of the numbers from 1-1000 that have a 3 in them
print([x for x in numbers if '3' in str(x)])


# Count the number of spaces in a string
sentence = 'Count the number of spaces in a string'
print(len([x for x in sentence if x == ' ']))


# Remove all of the vowels in a string
vowels = 'AaEeIiOoUu'
print(''.join([x for x in sentence if x not in vowels]))


# Find all of the words in a string that are less than 4 letters
print([x for x in sentence.split() if len(x) < 4])


# Use a dictionary comprehension to count the length of each word in a sentence.
print({word: len(word) for word in sentence.split()})


# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by