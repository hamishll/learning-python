# VARIABLE ASSIGNMENT
integer    = 1
string     = "mystring"
list       = [1, 2, 3]
tuple      = (item1, item2, item3)
dictionary = {key1 : value1, key2 : value2}

# ACCESSING VARIABLE VALUES
value = list[4]
value = list[1:2]
value = string[0:3]
value = dictionary[key]

# SPLITTING STRINGS

word = "Hamish"

print(len(word)		#-> 6
print(word[:3])		#-> Ham
print(word[2:])		#-> mish
print(word[:-1])	#-> Hamis

# FINDING, CHECKING TYPES AND REPLACING

print(word.find("Ham")) #-> 0
print(word.isalpha())   #-> true
print(word.isnum())		#-> false

