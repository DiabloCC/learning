# This script is to test various data types

## String
#a='Am I a string?'
#print("The value of a is:",a)
#print("The type of variant a is",type(a),".\n")
#
## Integer
#a=20
#print("The value of a is:",a)
#print("The type of variant a is",type(a),".\n")
#
## Float
#a=

# This String Format test
age=20
name='Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name,age))

print('Why is {0} playing with that python?'.format(name))

# format strings
# {0:0.x} x means the number of valid digits in the result includes has 
age=21.5
print('His age is {0:.7}.'.format(age/3))
print('{0} in float format is {1:.6}'.format('1/7',1/7))

# {0:a^x} means to format a string with a header and a tail
# a is the padding string and x is the formatted string length
# This test shows that if the 'x' minus the length of the original string
# get an odd number then the additional tail in formatted string
# will be longer than the header.  
print('{0:1^12}'.format('hello'))

#print argument
print('a',end="$&|")
print('b',end="...")


# Done
