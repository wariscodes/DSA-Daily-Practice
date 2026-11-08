# Q. BASIC PALINDROME IN STRING CHECK ????

# APPROCH 1(BRUTE FORCE)
name = input("Enter a name :")
rev = ""           # MAKE A EXTRA SPACE SO O(n)

for ch in name:  #ONE LOOP SO TIME IS O(n)
    rev = ch + rev # REVSERSE A STRING..  AND TIME IS O(N)

if name == rev:
    print("Its a Palindrome....") # OR RETURN TRUE WHEN ITS A PALINDROME
else:
    print("Not a Palindrome....") # # OR RETURN FALSE WHEN ITS NOT A PALINDROME
    
# TIME COMPLEXITY = O(n ** 2)
# SPACE COMPLEXITY = O(n)

# APPROCH 2(USING TWO POINTER)
name = input("Enter a name:")
left = 0
right = len(name) - 1

while left < right :
    if name[left] != name[right]:
        print("Not a palindrome....")
        break
    left += 1
    right -= 1
print("Its a palidrome....")

# TIME COMPLEXITY = O(n)
# SPACE COMPLEXITY = O(n)