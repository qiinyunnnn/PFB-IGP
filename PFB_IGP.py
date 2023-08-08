
from pathlib import Path
import csv

fp = Path.cwd() / 'csv_reports' / 'Overheads.csv'

with fp.open(mode='r', encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    Overheads = [] # Creates an empty list to store data of the overheads 
    for row in reader:
        Overheads.append([row])

def find_highest_overhead():
    '''
 This function is for calculating the highest overhead and printing out the percentage and name of it 
    '''
    
    highest_overhead = Overheads[0] # Assigns the first element of the Overheads list to highest_overhead
    for Overhead in Overheads:
        percentage = float(Overhead[0][1])  # Converts the percentage string to a float
        highest_percentage = float(highest_overhead[0][1])  # Convert the percentage string to a float
        if percentage > highest_percentage: # Checks if the current percentage of overhead is higher than the one selected at the start
            highest_overhead = Overhead # Assigns a new, larger percentage if the current overhead is lower than the next one it is compared to 
    return highest_overhead
highest_overhead = find_highest_overhead() #
name_of_overhead = highest_overhead[0][0] # Takes the first element from the nested list and assigns it to name_of_expense
percentage_of_overhead = highest_overhead[0][1] # Takes the second element from the nested list and assigns it to percentage_of_expense
print(f"[HIGHEST OVERHEAD] {name_of_overhead}: {percentage_of_overhead}%") # Prints out the name and percentage of the highest overhead

find_highest_overhead() # Call the function to perform the calculations and display results









