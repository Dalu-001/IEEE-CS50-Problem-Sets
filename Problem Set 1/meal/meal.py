def main():
    meal_time = convert(input("What time is it: ")) 

    if (meal_time >= 7.0 and meal_time <= 8.0):
        print("breakfast time")
    elif (meal_time >= 12.0 and meal_time <= 13.0):
        print("lunch time")
    elif (meal_time >= 18.0 and meal_time <= 19.0):
        print("dinner time")
    else:
        print("input a correct time.")



def convert(time):
    hour, minute = time.split(":")
    min_to_hour = float(minute)/60
    total = float(hour) + min_to_hour
    return total

if __name__ == "__main__":
    main()
