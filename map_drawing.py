# Kainoa Gaddis (c) 2014
# Map Drawing assignment

from turtle import *

# Open oregon map file
city_map = open("oregonmap.csv", "r")

# Find number of lines in the file
num_lines = 0
for line in open("oregonmap.csv"):
    num_lines += 1

# Create dictionary of city coordinats to use later
city_dict = {}

# Code to draw cities
def draw_city():
    # Make city dictionary to reference
    city_dict[city[1]] = city[2] + " " + city[3]

    # Pick up pen
    up()
        
    # Go to coordinate location
    goto(float(city[2]), float(city[3]))

    # Put down pen
    down()

    # Draw filled circle
    if int(city[4]) > 90000:
        begin_fill()
        circle(4)
        end_fill()

    # Draw Hollow circle
    elif int(city[4]) > 1 and int(city[4]) <= 90000:
        circle(2)

    # Only write name if it is a city
    if city[1][0] != "_":

        # Write city name near circle
        # I want to city to be even more left
        write(city[1], align = "left")

def draw_road():
    up()

    # Find beginning and end coordinated for roads
    location_beg = city_dict[city[1]].split(" ")
    location_end = city_dict[city[2]].split(" ")

    # Draw roads
    goto(float(location_beg[0]), float(location_beg[1]))
    down()
    goto(float(location_end[0]), float(location_end[1]))
    

# Main loop
for i in range(num_lines):
    # Reads a line off the file, remove \n and splits string into list
    city = city_map.readline().rstrip().split(",")
    
    # Code to draw cities
    if city[0] == "c":
        draw_city()

    # Code to draw roads
    elif city[0] == "r":
        draw_road()

done()




"""
Notes

import csv file

Have to set up a read function loop to read the next line

for each line
    separate the string by each comma
    if it is a city do a function
    same for road

city function
    go to location at 3rd and 4th index
    at a certain distance from the location print the name from index 2
    if population at index 5 is greater than 90,000
        draw larger filled circle
    elif population between 1 and 90,000
        draw small hollow circle
    
    if name starts with _ then do not print it 


"""
