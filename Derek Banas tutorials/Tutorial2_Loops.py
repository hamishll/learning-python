# ---------------------------------------------------------------------
# http://www.newthinktank.com/2016/06/learn-program-2/
# ---------------------------------------------------------------------
# PROBLEM 1: PRINT ODDS FROM 1 TO 20

for i in range(1, 20):
    if ((i % 2) != 0):
        print("i =", i)

# ---------------------------------------------------------------------
# WORKING WITH FLOATS

my_float = input("Enter a float: ")
my_float = float(my_float)

print("Rounded to 2 decimals : {:.2f}".format(my_float))

# PROBLEM 2: COMPOUNDING INTEREST
# Have user input their investment amount and expected interest
money = input("How much do you want to invest?")
interest_rate = input("What is your expected rate of return?")

money = float(money)
interest_rate = float(interest_rate) * 0.01

for i in range(10):
    print(money)
    money = money + (money * interest_rate)

print("Investment after 10 years: {:.2f}".format(money))

# ---------------------------------------------------------------------
# WORKING WITH FLOATS
# Floats are not precise! the following should print 0 but it doesn't

i = 0.1 + 0.1 + 0.1 - 0.3
print(i)

# This is because values below 0 can't
# always be resolved exactly in binary

# ---------------------------------------------------------------------
# THE WHILE LOOP
# Will keep looping as long as the condition is true

# PROBLEM 3: DRAW A PINE TREE
# Draw a pine tree after asking the use for the number of rows
tree_height = input("How tall is your tree?")
tree_height = int(tree_height)

# Starting values
spaces = tree_height - 1
hashes = 1

# Stump values
stump_spaces = tree_height - 1

while tree_height != 0:

    for i in range(spaces):
            print(' ', end="")

    for i in range(hashes):
            print('#', end="")

    #insert new line
    print()

    spaces -= 1
    hashes += 2
    tree_height -=1

for i in range(stump_spaces):
    print(' ', end="")

print('#')

