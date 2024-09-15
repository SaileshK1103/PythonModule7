#7. Tuple,Set and Dictionary
#7.1 Write a program that asks the user for a number of a month and then prints out the corresponding
# season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.
import numbers


def generateSeasonTuple():
    seasons = ()
    numbers = int()
    while True:
        season = input("Enter the name of different seasons: ")
        if season =="":
            break
        else:
            seasons += (season,)
    return seasons
getSeasons = generateSeasonTuple()
while True:
    month = int(input("Enter the number of a month (1-12): "))
    if month =="":
        break
    elif (1<=month<=12):
        season = getSeasons[month-1]
        print(f"The corresponding season is {season}")
    else:
        print("please enter a valid month number between 1-12")

