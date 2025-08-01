# List of numbers
numbers = [4, 7, 2, 4, 9, 2, 7, 10, 4]

# Create an empty dictionary to store counts
count = {}

for num in numbers:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
        
print("Duplicate elements: ")

for num in count:
    if count[num]>1:
        print(num)