
# Strings can be inserted by index position as well
print(" This is a string {}" .format('INSERTED'))

print("The {} {} {}" .format('fox', 'brown', 'quick'))

# The curly brackets reflect the position i can put it into a string.
print("The {2} {1} {0}" .format('fox', 'brown', 'quick'))



Test1 = "Hello"

Test2 = "Bye"


Test3 = "Good morning"
print("The {f} {b} {q}" .format(f='F', b = 'B', q = 'Q'))


# another way to do this
print(f" Here are some index position inserts, {Test1} {Test2} {Test3} ")



print('---------------------------')
result = 104.12345
print(result)
# This is the long number....


#Value of precision
#Value: width.precision f)

print("the result was {r:1.3f} " .format(r=result))

# White Space. will be added. The width describes you want the string to be
print("the result was {r:10.3f} " .format(r=result))
# more often we will mess with precision.


name = "Jose "
# format F infront. then insert name at end.
print(f'Hello, his name is {name}')

NameTest = "Sam"
age = 3
print(f'{name} is {age} years old')