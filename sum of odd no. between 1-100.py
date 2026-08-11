# Sum of odd numbers between 1 and 100

n = int(input("Enter the value of n:"))

for i in range(1,101) :
    if i % 2 != 0 :
        print(i)
