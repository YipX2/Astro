#import flatlibfr
import time 
day = int(input("What day were you born?\n"))
month = input("What month were you born?\n").upper()
year = input("What year were you born?\n")
#months = ["Placehold", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sun_sign = ()

if month=='January' or month=='Jan' or month=='01' or month=='1':
    month = 'January'
    if day < 19:
        print("You're an Aquarius!")
        sun_sign = 'Aquarius'
    else:
        print("You're a Capricorn!")
        sun_sign = 'Capricorn'
if month=='Febuary' or month=='Feb' or month=='02' or month=='2':
    month = 'Febuary'
    if day < 19:
        print("You're an Aquarius!")
        sun_sign = 'Aquarius'
    else:
        print("You're a Pisces!")
        sun_sign = 'Pisces'
if month=='March' or month=='03' or month=='3':
    month = 'March'
    if day < 21:
        print("You're a Pisces!")
        sun_sign = 'Pisces'
    else:
        print("You're an Aries")
        sun_sign = 'Aries'
if month=='April' or month=='04' or month=='4':
    month = 'April'
    if day < 20:
        sun_sign = 'Aries'
        print("You're an Aries!")
    else:
        sun_sign = 'Taurus'
        print("You're a Taurus!")
if month=='May' or month=='05' or month=='5':
    month = 'May'
    if day < 21:
        sun_sign = 'Taurus'
        print("You're a Taurus!")
    else:
        sun_sign = 'Gemini'
        print("You're a Gemini!")
if month=='June' or month=='06' or month=='6':
    month = 'June'
    if day < 21:
        sun_sign = 'Gemini'
        print("You're a Gemini")
    else:
         sun_sign = 'Cancer'
         print("You're a Cancer!")
if month=='July' or month=='07' or month=='7':
    month = 'July'
    if day < 23:
        sun_sign = 'Cancer'
        print("You're a Cancer!")
    else:
        sun_sign = 'Leo'
        print("You're a Leo!")
if month=='August' or month=='08' or month=='8':
    month = 'August'
    if day < 23:
        sun_sign = 'Leo'
        print("You're a Leo")
    else:
        sun_sign = 'Virgo'
        print("You're a Virgo")
if month=='September' or month=='Sept' or month=='09' or month=='9':
    month = 'September'
    if day < 22:
        sun_sign = 'Libra'
        print("You're a Libra")
if month=='October' or month=='Oct' or month=='10':
    month = 'October'
    if day < 24:
        sun_sign = 'Libra'
        print("You're a Libra")
    else:
        sun_sign = 'Scorpio'
        print("You're a Scorpio")
if month=='November' or month=='Nov' or month=='11':
    month = 'November'
    if day < 22:
        sun_sign = 'Scorpio'
        print("You're a Scorpio")
    else:
        sun_sign = 'Sagittarius'
        print("You're a Sagittarius")
if month=='December' or month=='Dec' or month=='12':
    month = 'December'
    if day < 22:
        sun_sign = 'Sagittarius'
        print("You're a Sagittarius")
    else:
        sun_sign = 'Capricorn'
        print("You're a Capricorn")

#birthday = (str(month  + day  + year))

#print(f"Your birthday is {month}, {day}, {year}")