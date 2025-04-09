# Beneath each comment write the code and print out the result to check it works

'''LISTS'''

# Create a list and assign it to a variable

list_random = [1, 3, 5, 7, 9]
print(list_random)

# Find the length of the list

list_length = len(list_random)
print(list_length)

# Append an item to the list

list_random.append(11)
print(list_random)

# Find the value of an item in the list a specific index

index = 3
value_index = list_random[3]
print(value_index)

# Set the value of an item at a specific index

item = 111
index = 4
list_random[4] = item
print(list_random)

# Check whether an item is in the list

if item in list_random:
    print("True")
else:
    print("False")

# Sort the list

list_random.sort()
print(list_random)

# Iterate over the list using range, printing out each element and the index

for index in range(len(list_random)):
    print(index, list_random[index])

# Iterate over the list without using range, printing out each element

for item in list_random:
    print(item)


    '''TUPLES'''

# Create a tuple and assign it to a variable

tuple_random = ('one', 'two', 'three')
print(tuple_random)

# Find the length of the tuple

tuple_length = len(tuple_random)
print(tuple_length)

# Find the value of an item in the tuple a specific index

index = tuple_random[2]
print(index)

# Check whether an item is in the tuple

item = '4'
if item in tuple_random:
    print("True")
else:
    print("False")

# Iterate over the tuple using range, printing out each element and the index

for index in range(len(tuple_random)):
    print(index, tuple_random[index])


# Iterate over the tuple without using range, printing out each element

for item in tuple_random:
    print(item)


    '''STRINGS'''

# Create a string and assign it to a variable

word = "Hello World!"
print(word)

# Find the length of the string

length_str = len(word)
print(length_str)

# Find the value of an character in the string a specific index

index = 6
value_of_index = word[index]
print(value_of_index)

# Check whether an item is in the string

if "W" in word:
    print("True")
else:
    print("False")

# Concatenate (add) two strings together

word_2 = "!!"
word_total = word + word_2
print(word_total)

# Create an f-string

print(f"My string is {word_total}")

# Split a string using .split

new_word = word.split()
print(new_word)

# Join a list of strings using .join

other_word = ' '.join(new_word)
print(other_word)

# Iterate over the string using range, printing out each character and the index

for index in range(len(word)):
    print(index, word[index])

# Iterate over the string without using range, printing out each character

for letter in word:
    print(letter)


    '''DICTIONARIES'''

# Create a dictionary and assign it to a variable

dict = {
    "apple": 1, 
    "orange": 3
    }
print(dict)

# Find the length of the dictionary

len_dict = len(dict)
print(len_dict)

# Add a new key/value pair

dict["pear"] = 3
print(dict)

# Replace value for a given key

dict["pear"] = 5
print(dict)

# Check whether a key is in the dictionary

if "pear" in dict:
    print("True")
else:
    print("False")

# Iterate over keys, printing each key

for key in dict.keys():
    print(key)

# Iterate over over key/value pairs using .items(), printing each key and value

for key, value in dict.items():
    print(key, value)


'''SETS'''

# Create a set and assign it to a variable

my_set = {"apple", "pear"}
print(my_set)

# Find the length of the set

len_set = len(my_set)
print(len_set)

# Add a new element

new_set = my_set.add("orange")
print(my_set)

# Remove an element

other_set = my_set.remove("pear")
print(my_set)

# Check whether a element is in the set

if "apple" in my_set:
    print("True")
else:
    print("False")

# Iterate over elements, printing each one out

for el in my_set:
    print(el)


    '''NUMBERS'''

# Add / subtract / multiply 2 numbers
a = 10
b = 20
add_num = a + b
sub_num = a - b
mult_num = a * b
print(add_num)
print(sub_num)
print(mult_num)

# Divide two numbers using normal (float) division

div_fl = a / b
print(div_fl)

# Divide two numbers using integer division

div_num = a // b
print(div_num)

# Find the modulo (remainder) of two numbers

mod_num = b % a
print(mod_num)

# Check whether a number is even/odd

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# Round a float down to an int

c = 2.4
down = int(c)
print(down)


'''FUNCTIONS'''

# Write a function that takes no arguments and call it

def first_f():
    print("hi")
first_f()

# Write a function that takes one or more arguments and call it

def sum(a, b):
    print(a + b)
sum(2, 4)

# Write a function that returns a value. Call the function and store the return value in a variable

def sum(a, b):
    sum = a + b
    return sum
res = sum(23, 67)
print(res)


'''LOOPS'''

# Write a while loop

count = 1
while count < 10:
    count += 1
print(count)

# Write a for loop that loops a set number of times (e.g. 10 times)

my_set = {"apple", "banana", "cherry"}

for fruit in my_set:
    print(fruit)

    '''CONDITIONALS'''

# Write an if/elif/else statement

a = 1
b = 3
c = 10
if a > b:
    a += 1
elif a > c:
    a -= 5
else:
    a += 20
print(a)

# Write conditionals for the following operators:
# ==
a = 1
b = 1
print(a == b)

# !=
a = 1
b = 2
print(a != b)


# <
a = 1
b = 2
print(a < b)

# >
a = 3
b = 2
print(a > b)

# <=
a = 1
b = 2
print(a <= b)

# >=
a = 2
b = 2
print(a >= b)

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable

nl = [['apple','orange'], ['beans', 'cabbage']]
print(nl)

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second

ind = 1
inner_ind = 0
item = nl[1][0]
print(item)

# Iterate through the nested data structure using range

for ind_1 in range(len(nl)):
    for ind_2 in range(len(nl[ind_1])):
        print(nl[ind_1][ind_2])

# Iterate through the nested data structure without using range 

for inner_list in nl:  
    for element in inner_list:  
        print(element)

'''REMINDER'''

# You're doing great and you got this!
