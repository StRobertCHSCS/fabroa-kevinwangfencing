# get the number of marks
number = int(input("Enter the number: "))

# initialize total
total = 0

#compute the total from 1 to a number 
for i in range(1, number+1, 2):
    #print(1)
    total = total + i

#compute average based on total
print(total)