# Ask for the tempurtare

temperature = int(input("Enter today's tempurtare in Celsius: "))

#PART 2: Decide between a jacket and a t-shirt 
if temperature< 20:
  outfit = "jacket"
  print("it is cold today")
  print("wear a", outfit)
else:
  outfit = t-shirt 
  print("it is warm today")
  print("wear a ", outfit)

# part:3 Ask wether it is raining
is_raining = input("it is raining today?  ( YES / NO): ")

# PART:4 Add an umbrella reminder only if it is raining
if is_raining == "YES": 
  print("bring an umberala")

# part 5: Ask for the wind speed
wind_speed = int(input("enter the wind speed in Km/H : "))                        

#part:6: Decide wether a windbraker is needed
if wind_speed > 30:
  needs_windbraker = "YES"
  print("its windy today")
  print("wear a windbraker over your", outfit)
elce:
  needs_windbraker
  print("it is wiedly")