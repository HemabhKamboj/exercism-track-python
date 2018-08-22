
    
def is_leap_year(year):
  
    if (year%4==0):
        print ("{} is leap year in Georgian calendar".format(year))

    elif (year%100==0) and (year%400==0):
        print ("{} is leap year in Georgian calendar".format(year))

    else :
        print("{} is not a leap year".format(year))


year = input("Enter the year")
is_leap_year(year)
##def run_is_leap_year():
  ##  year = int(input("Enter the year"))
    ##is_leap_year(year)
