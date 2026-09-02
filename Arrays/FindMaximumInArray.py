# Find tha Maximum/Largest Element in Array?
# Via Indexing

arr = [2 , 8 , 10 , 4 , 7 , 20 , 100 , 30 , 50]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
        
print("Largest Element in Array :",largest)

# Direct Normal Element

largest = 0

for i in arr:
    if i > largest :
        largest = i
print("Largest Element :" , largest)