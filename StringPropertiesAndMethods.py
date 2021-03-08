
name = "Sam"
## This will error
#Commented out ======  name[0] = "P"
last_letters = name[1:]

NewWord = 'P' + last_letters
print(NewWord)
print(last_letters)

x = ' Hello World '
y = "  It is beautiful outside "
z = x + y
print(z)



##################

# Taking two strings and combining them. String concatination. In the jupitor notebook. He was able to just have the same word.
# I am not sure if thats because of the notebook. I get same result different way.
letter = 'a'
letter10 = letter * 10
print(letter10)


print("------------------")
print(2 + 3)

print("2" + "3")

x = "Hello World"
# set x to = upper case
x = x.upper()
print(x)

x = x.lower()
print(x)

# For some reason i have to create a new variable to split
g = "Hi this is a string"
c = g.split()
print(c)

# remember this. I sometimes had to make a new variable. 
print('----')
b = g.split('i')
print(b)
