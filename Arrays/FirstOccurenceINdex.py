# Find the first Occurence index in arrays ?

arr = [2 , 4 , 7 ,9 , 10]
num = int(input("Enter number :"))
found = False

for i in range(len(arr)):
    if arr[i] == num:
        print("Index :",i)
        found = True
        break

if not found:
    print("Not Found")
    
# Time complexity = O(n)
# Space Complexity = O(1)    