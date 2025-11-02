speed = int(input("Input your speed:"))
unit = input("Input the unit(km/h, mph:)")

speed_limit_kmh = 60
speed_limit_mph = 37

if speed <= speed_limit_kmh and unit == "km/h":
    print("You aren't going over the speed limit!")
    
elif speed > speed_limit_kmh and unit == "km/h":
    print("You're going too fast! Slow down!")
    
elif speed <= speed_limit_mph and unit == "mph":
    print("You aren't going over the speed limit!")
    
elif speed > speed_limit_mph and unit == "mph":
    print("You're going too fast! Slow down!")
    
else:
    print("Invalid unit or speed.")