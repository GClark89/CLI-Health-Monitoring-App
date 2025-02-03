# Create a list to store data
heart_rate = []

# Take in the name of the participant
name = input("What is your name? ")
# Capitalize their name
name = name.capitalize()
# greet them with their name: "Hello 'name', please prepare your heart rate data."
print("Hello " + name + ", please prepare your heart rate data.  ")

# Take in hour one heart rate
hour1 = int(input( "Please provide your heart rate at hour 1: "))
# Append this integer value to the list
heart_rate.append(hour1)

# Take in hour two heart rate
hour2 = int(input("Please provide your heart rate at hour 2: "))
# Append this integer value to the list
heart_rate.append(hour2)


# Take in hour three heart rate
hour3 = int(input("Please provide your heart rate at hour 3: "))
# Append this integer value to the list
heart_rate.append(hour3)

# Take in hour four heart rate
hour4= int(input( "Please provide your heart rate at hour 4: "))
# Append this integer value to the list
heart_rate.append(hour4)

# Take in hour five heart rate
hour5 = int(input( "Please provide your heart rate at hour 5: "))
# Append this integer value to the list
heart_rate.append(hour5)

# Take in hour six heart rate
hour6= int(input("Please provide your heart rate at hour 6: " ))
# Append this integer value to the list
heart_rate.append(hour6)

# Take in hour seven heart rate
hour7= int(input("Please provide your heart rate at hour 7: "))
# Append this integer value to the list
heart_rate.append(hour7)

# Take in hour eight heart rate
hour8 = int(input ( "Please provide your heart rate at hour 8: "))
# Append this integer value to the list
heart_rate.append(hour8)
# Thank them: "Thank you 'name', we will now calculate your health metrics."
print( "Thank you " + name  , "we will now calculate your health metrics...")

# Get the maximum heart rate from your list, save into a variable
maximum = max(heart_rate)
# print out the patients maximum heart rate during sleep
print("Maximum heart rate is " + str(maximum))
# Get the minimum heart rate from your list, save into a variable
minimum = min(heart_rate)
# print out the patients minimum heart rate during sleep
print("Minimum heart rate is " + str(minimum))

# Calculate the difference between these values
Difference = (maximum - minimum)
# print out this difference
print("your difference is " + str(Difference))

# if this difference is greater than 30, print that they experienced waking during sleep
if Difference > 30:
    print ("you experienced waking during sleep")
# if this difference is greatert han 20, print that their HRV is in a healthy range
if Difference > 20:
    print("Your HRV is in Healthy range ")
# otherwise, print out that their HRV is low and might indicate sleep issues
else:
    print( "HRV IS Low and might indicate sleep issues")

# print out their entire heart rate data
print ("Here is your entire heart rate data " + str(heart_rate))
