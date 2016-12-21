# -----------------------------------------------------------------------------------------
# Forcing a user to enter a number (and not a string or alphabet)
# -----------------------------------------------------------------------------------------

while True:

    try:
        number = int(input("Please enter a number:"))
        break

    except ValueError:
        print("You didn't enter a number")

    except:
        print("An unknown error occurred")

print("Thank you for entering the number {}".format(number))

# -----------------------------------------------------------------------------------------
# DO/WHILE LOOPS - always execute code at least once, will run again if conditions met
# -----------------------------------------------------------------------------------------

secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 10 : "))

    if guess == secret_number:
        print("You guessed it")
        break

# ----------------------------------------------------------------------------------------
# A more complex version
# ----------------------------------------------------------------------------------------

secret_number = 7

while True:

        try:
            guess = int(input("Guess a number between 1 and 10:"))
            if guess == secret_number:
                print("You guessed it!")
                break

            elif guess != secret_number:
                print("Guess again!")

        except ValueError:
            print("You didn't guess a number!")

        except:
            print("An unknown error occurred")

# -----------------------------------------------------------------------------------------
# Using the MATH Module
# -----------------------------------------------------------------------------------------

import math

ceil = math.ceil(4.7)           # rounds up                 5
floor = math.floor(4.7)         # rounds down               4
fabs = math.fabs(-4.7)          # absolute value            4.7
factorial = math.factorial(4)   # factorial                 1*2*3*4 = 24
fmod = math.fmod(5,4)           # remainder of division     5/4 = ...remainder = 1
trunc = math.trunc(4.7)         # returns an integer        4
pow = math.pow(2,2)             # to the power of           x^y
sqrt = math.sqrt(4)             # square root               2
e = math.e                      # e                         2.71...
pi = math.pi                    # pi                        3.14...
exp = math.exp(4)               # exponent e^x              54.59...
log = math.log(20)              # natural log               e^? = 20
log10 = math.log(1000,10)       # defining base as 10       log10(1000) = 3
sin = math.sin(90)              # trig functions            1
deg = math.degrees(1.56)        # converts rad to deg       90
rad = math.radians(90)          # converts deg to rad       1.57...

# -----------------------------------------------------------------------------------------
# Importing individual methods (Decimal) from modules (decimal), and reassigning name (D)
# -----------------------------------------------------------------------------------------

from decimal import Decimal as D

# Decimal avoids the inaccuracy of math operations on floats
sum = D(0)

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum =", sum)

# -----------------------------------------------------------------------------------------
# Type
# -----------------------------------------------------------------------------------------
                        # Output:
print(type(3))          # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type('words'))    # <class 'str'>

# -----------------------------------------------------------------------------------------
# Referencing index of a string
# -----------------------------------------------------------------------------------------
mystring = "Words go here"

print(mystring[0])      # W
print(mystring[-1])     # e
print(mystring[3+5])    # h
print(mystring[2:7])    #rds g

# Cycle through characters in pairs
# Subtract 1 from the length because length is 1 more then the highest index
# because strings are 0 indexed
# Use range starting at index 0 through string length and increment by
# 2 each time through
for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

# ---------- PROBLEM : SECRET STRING ----------
# Receive a uppercase string and then hide its meaning by turning
# it into a string of unicode
# Then translate it from unicode back into its original meaning
# ---------------------------------------------

# input_string = input("What is your string?")
# unicode_string = ''
#
# for i in range(0, len(input_string)-1, 1)

#    unicode_string = unicode_string + str(ord(input_string[i]))

# print(unicode_string)
