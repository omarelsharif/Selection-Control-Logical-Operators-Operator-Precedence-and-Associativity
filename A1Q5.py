#Question 5


temp = input("Enter the temperature in Farenheit betweeen -58 and 41: ")
temp = float(temp)
speed =input("Enter the wind speed miles per hour (must be greater than or equal to 2): ")
speed=float(speed)
windchill_index = 35.74 + (0.6215 * temp) - (35.75 * (speed**0.16)) + 0.4275*temp*(speed**0.16)
windchill_index = round(windchill_index, 2) 
print ("The wind chill index is", windchill_index)
