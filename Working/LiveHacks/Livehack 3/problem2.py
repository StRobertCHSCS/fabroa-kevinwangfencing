#initalize counter
number_days = 0
total_distance = 0
daily_distance = 0

#loop to get user amounts and accumlate total
while daily_distance != -1:
    daily_distance = float(input("Enter a daily distance:"))
    total_distance = total_distance + daily_distance
    number_days = number_days + 1

    if total_distance >= 100:
        average = total_distance/number_days
        print(" The average of " + str(number_days) + " days is " + str(average) )