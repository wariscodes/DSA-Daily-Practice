# Q. Count the Vowel in given String.......

name = "Education is important"
count = 0

for ch in name:
    if ch in "aeiou":
        count += 1
        
print("Vowels count is :",count)


# Q. Count the Consonent in given String.....

name = "Education is important"
count = 0

for ch in name:
    if ch not in "aeiou":
        count += 1
        
print("Consonent count is :",count)