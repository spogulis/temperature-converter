#Program greets user and describes what's the purpose of the program
print("Hello! This is a small app that will help you convert Celsius values into Farenheit.")
input("Press any key to begin!")

#Program asks user to enter number of kilometers, user enters data and it's stored in temperatureF variable
temperatureInput = input("Please enter the Celsius temperature")
temperatureInput = float(temperatureInput)

#Calculate Farenheit from Celsius
temperatureF = temperatureInput * 1.8 + 32
print(str(temperatureInput) + "C equals to  " + str(temperatureF) + "F")

