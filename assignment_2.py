""" 1) Create a list of names and use a for loop to output
the length of each name (len() ).

2) Add an if  check inside the loop to only output
 names longer than 5 characters.

3) Add another if  check to see whether a name includes
 a “n”  or “N”  character. """

names = ["kannan", "leon", "kimberly", "saNdra", "ricky"]

for name in names:
    if len(name) > 5 and "n" in name.lower():
        print(name, len(name))
# 4) Use a while  loop to empty the list of names (via pop() )
while names:
    print(names.pop())
