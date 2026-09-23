#Information
username = str(input("What is your name? "))
destination = str(input("Where are you travelling to? "))
distance = float(input("How many miles away is that? "))
Miles_Per_Gallon = float(input("How many miles per gallon does your car give you? "))
Gas_Price = float(input("How expensive will gas be? "))
Number_of_Travellers = int(input("How many people will you travel with? "))

#Calculations
Total_Distance = distance*2
Needed_Gas = distance/Miles_Per_Gallon
Total_Gas_Cost = Gas_Price*Needed_Gas
Cost_Per_Traveler = Total_Gas_Cost/Number_of_Travellers

#Display
print("\n--- ROAD TRIP COST SUMMARY ---")
print(f"Traveler: {username}")
print(f"Destination: {destination.upper()}")
print(f"Total miles: {Total_Distance}")
print(f"Gallons of gas needed: {Needed_Gas:.2f}")
print(f"Total estimated cost: ${Total_Gas_Cost:.2f}")
print(f"Estimated cost per traveler: ${Cost_Per_Traveler:.2f}")
print("-------------------------------")
print(f"Have fun in {destination.upper()}!")