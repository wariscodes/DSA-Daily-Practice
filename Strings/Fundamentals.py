# Basic Fundaments of string....
# Q. Find length of given string?

name = "Jack Michel" # Space also count in length
print(len(name))

# Indexing...

name = "Jack Michel"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[5])
print(name[6])

# Slicing .....

name = "Jack Michel"
print(name[0:3]) # Last character does'nt included in slicing
print(name[1:3])
print(name[:4]) #Start from 0 automentically
print(name[0:]) #Run to the end of the string

# Transversal(like a loop)

name = "Jack Michel"
for char in name:
    print(char) #ouput - J a c k M i c h e l
    
# Sting Immutable (Does'nt change directlt)

# name = "Jack Michel"
# name[0] = "M"
# print(name) # It does't change because it is immutable we create another sring for changing...

name = "Jack Michel"
name = "M" + name[1:] # It can changeble because we create diffrent string...
print(name) # Output - Mack Michel

# Operatorss

first_name = "Jack"
last_name = "Michel"
full_name = first_name +" "+last_name
print(full_name)  # Output - Jack Michel

# Repeat
letter = "Hii"
print(letter * 3) #HiiHiiHii  print 3 times

# Upper / Lower
name = "jack"
print(name.upper()) # output - JACK

name = "JACK"
print(name.lower()) # output - jack

# Split
name = "Jack Michel Denny"
result = name.split()
print(result)

# Find / Index
name = "Jacl Michel Denny"

print(name.find("Jack")) # Output - 5
print(name.index("Denny")) # Output - 11

# Replace
name = "Michel denny"
result = name.replace("Michel", "Jack") #('Oldname' , "Newname")

print(result) # Output - Jack Denny

# IN / NOT IN
name = "Jack Michel Denny"

print("Jack" in name) # True
print("Michel" in name) # True
print("Denny"not in name) # False

# isalpha() , isdigit() and isnumalpha()
name = "Jack"
number = "12345"
data = "Jack123"

print(name.isalpha()) # True (Only letters)
print(number.isdigit()) # True (Only Digits)
print(data.isalnum()) # True (Both Digit and letters)


# String comparison
name1 = "JACK"
name2 = "JACk"
name3 = "jack"

print(name1 == name2) # True
print(name1 == name3) # False (Because python string is case sensitive)
print(name1 != name3) # True