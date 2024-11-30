def leap_year(year):
    if(year %4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    else:
        return False
while True:
    try:
        user_input = input("Enter a year:")
        year = int(user_input)
        if leap_year(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
        break;
    except ValueError:
        if '/' in user_input: 
            print("Please insert a valid year without /.")
        else:    
            print("Please insert a valid year in correct format (numeric value).")
    
    
