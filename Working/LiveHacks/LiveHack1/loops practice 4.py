
#get the number
start = int(input("enter the starting number"))
end = int(input("enter the ending number"))

# output range
if start < end:
    for i in range(start, end+1, 1):
        print(i)

else:
    for i in range(start, end-1, -1):
        print(i)