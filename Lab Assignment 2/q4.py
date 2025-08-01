user_input=input("Enter the numbers separated by space: ")
numbers = list(map(int,user_input.split()))
print("You entered:", numbers)


print("Even numbers in the list are: ")
for num in numbers:
    if(num%2==0): 
        print(num)