# Find the Minimum Elements in Array?

arr = [2 , 8 , 10 , 4 , 7 , 20 , 100 , 30 , 50]
smallest = arr[0]

for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = i
        
print("Smallest Element are :",smallest)

# Time Complexit = O(n)
# Space Complexity = O(1)