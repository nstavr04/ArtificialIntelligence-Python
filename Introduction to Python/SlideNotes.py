# Notes from the Slides.

# For multi line strings use """a'b"c"""

# Multiple assignments

x,y = 2,3
print(x)
print(y)

# Tuple and Strings are immutable, Lists are mutable

# Tuple
tu = (23,'abc',4.56,(2,3), 'def')
print(tu)
print(tu[1])

# List
li = ["abc", 34, 4.34, 23]
print(li)
print(li[1])
print(li[-1])
# Can return a copy of a subset within a range, can use -1 etc as well
print(li[1:])
# Copy whole subset
print(li[:])

# Boolean Test, Lists, Tuples and for substrings etc
print(3 not in li)
print(34 in tu)

# Can use + to concatenate list, tuple, strings into a NEW one
# Can use * to produce a NEW list, tuple, string that repeats the original content
print(li*3)

# We can change list contents, we cannot change tuple contents tho
li[1] = 3
# Can use .append('a') , .insert(2,'i') , .extend([9,8,7]) 
# To append vazei oti valw mesa san 1 stixeio tis listas, ara an doso lista tha exw lista se lista
# To extend prosthetei sto telos ena ena ta antikimena p edosa
print(3 not in li)

# Lists exun methods polla, px , index,count,remove,reverse,sort

# Dictionaries, they are a mapping between a set of keys and a set of values
dic = {'user': 'bozo', 'pswd': 1234}
print(dic['user'])
print(dic['pswd'])

# I can change the dictionary contents, eg d['user'] = 'clown'
# Dictionaries are unordered, we can add a new key but we don't know where it will get placed

# Can delete dictionary entries as well
del dic['user']
print(dic)
# dic.clear , you can remove all dictionary entries
# Can use .keys, .values, .items

# Defining Function
def myfun (x,y):
    return x * y
print(myfun(3, 4))

# There is no function overloading in Python, you can't have 2 function with the same name and different arguments
# Can use default values on functions, e.g myfun(b, c=3, d="hello")

# if and elif and else
if x == 3:
    print("Hello")
elif x == 2:
    print("X equals 2")
else:
    print("")

# Can use break as well, can use assert() to check while something is true, if its not the program stops

# for loops, we can iterate a collection, we can use for x in range(5) as well

# We can use string formatting to print as well like in C with the %

# We can use .join and .split in strings

# We can concatenate number with string, we type it e.g "Hello" + str(2)
    
