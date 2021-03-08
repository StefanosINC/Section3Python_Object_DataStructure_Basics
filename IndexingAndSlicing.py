my_string = "Hello World"
print(my_string)


# this is grabbing the first charachter in the print statement. In this case it would be H
print(my_string[0])

# indexing. grabs the R cuz its 8
print(my_string[8])

# I can reverse index . Look back start D as -1  then work your way back.
print(my_string[-4])

print(my_string[-1])


print("-------------------------")

my_string = "abcdefghijk"
print(my_string)

# start at the index 2 and move toward the end.
print(my_string[2:])

# grabbing everything up to a particular index
# GO UP TO BUT NOT INCLUDE the 3. Especially with slicing
print(my_string[:3])

# Grab DEF
print(my_string[3:6])

#Grab BC
print(my_string[1:3])


# Step size. Grab everything from beginning to end
print("----------")
print(my_string[::])

# Jump size of 2. A to C to E to G to I K
print(my_string[::2])

# start at index 2. Work your way to index 7. Thats the parameters your working with. Now jump 2 every time. Print that out.
print(my_string[2:7:2])

print("reverse string")
# look at the entire list. start at -1
print(my_string[::-1])
# prints the entire list
print(my_string[::])

#String index
print('------Quiz Time-----')
print('Hello World'[8])


#String Slice
print('-- Quiz Time-----')
print("tinker"[1:4])
