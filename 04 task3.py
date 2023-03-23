# code to determine whether a triathlete qualifies for an award

# requests a times for three events and assigns to variables
swimming_time = int(input("Please enter your swimming time in minutes:\t"))
cycling_time = int(input("Please enter your cycling time in minutes:\t"))
running_time = int(input("Please enter your running time in minutes:\t"))

# adds times together and prints the total time 
total_time = swimming_time + cycling_time + running_time
print("\nYour total triathlon time is {} minutes".format(total_time))

if total_time <= 100:  # if within qualifying time
    print("You have been awarded Provincial Colours")
elif total_time <= 105:  # if within 5 mins of qualifying time
    print("You have been awarded Provincial Half Colours")
elif total_time <= 110:  # if within 10 mins of qualifying time
    print("You have been awarded Provincial Scroll")
else:  # if over 10 mins of qualifying time
    print("You have not recieved an award this time")