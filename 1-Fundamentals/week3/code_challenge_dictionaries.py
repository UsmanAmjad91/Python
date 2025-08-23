inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def total_snow(snow): 
    print("Total snowfall inches:", sum(snow.values()))

total_snow(inches_snow)

try:
    inches_snow["Thursday"] = int(input("Inches of snow on Thursday: "))
except ValueError:
    print("Invalid input. Using 0 inches.")
    inches_snow["Thursday"] = 0

total_snow(inches_snow)
