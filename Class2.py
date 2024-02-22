# Data types
country = "India"
age = 34
age = 'Hello'
salary = 345.3
isexists = False
print("")
# Python is dynamically data types language
# Based on the type of data , the python interpreter defined some data types
# Primitive Data types 
# string
# int 
# float
# bool

# string => it contains alphabets ,special character , numbers combination of all , it can contain any data . we
# should represent with " " or ' '
# str
address = "#12 ,Do .No 23 ,2nd Cross,AP"
state = "AP"

# int => it contains only numbers
x = 344
# float => it contains decimal values
intrest = 34455.34
# bool (boolean) => it contains two values , True or False
activate = True
deactivate = False

# type() => by using this we can get the type of data
print("Type of x :", type(x))

total = x + intrest  # 34+34455.34 => 34.00+34455.34 => 34799.34
print(total)
print("Type of total :", type(total))
name = 'chandra'
print("Type of name :", type(name))
print("Type of activate :", type(activate))

# Data Type conversions  => converting from one datatype to other datatype

# Implicit type conversion => Python interpreter will automatically convert to higher data type
total = x + intrest  # 34+34455.34 => 34.00+34455.34 => 34799.34
print(total)

# Explicit type conversion => we need to convert to specific data type

total = x + int(intrest)
print("total after conversion :", total)
print("total type :", type(total))

address = "#23,RamNagar,Anantapur"
pincode = 234555
complete_address = name + " " + address + " \n" + str(pincode)
print(complete_address)

data = "345"
print( int(data) + 45)
print(data + str(45) + str(True))
print(int(False))

name = '''
kxnklsdfkldng
dsglkdf
        '''