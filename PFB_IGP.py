from pathlib import Path
import csv
fp = Path.cwd()/'csv_reports'/"Profit_And_Loss.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    Profit_And_Loss = []
    for row in reader:
        Profit_And_Loss.append([row[0],row[4]])

def profit_loss_function():
    '''
    This function is for calculating the difference in the net profit column and prints out the day and amount the highest increment occurs
    '''
    difference_in_net_profit = [] # Creates an empty list to store
    # creates a for loop that iterates over a sequence of numbers starting from 1 up to the length of the "Profit_And_Loss" dataset
    for day in range(1, len(Profit_And_Loss)): 
         # retrieves the profit value for the current day and converts it to an integer, and assign it to the variable current_day_profit
        current_day_profit = int(Profit_And_Loss[day][1])
        # retrieves the profit value for the previous day and converts it to an integer, and assign it to the variable prev_day_profit
        prev_day_profit = int(Profit_And_Loss[day-1][1])
        # The calculated "difference" variable will store the profit differences between each consecutive day, representing how much profit increased or decreased from one day to the next
        difference = prev_day_profit - current_day_profit

        if difference > 0:
           difference_in_net_profit.append(f"[PROFIT DEFICIT] DAY: {Profit_And_Loss[day][0]}, AMOUNT: USD{difference}") #Appends the deficit  
    print(difference_in_net_profit) # Prints list to check if items in the list were printed out correctly 
    return difference_in_net_profit # Returns the difference_in_net_profit list to the function

profit_loss_function() # Call the function to perform the calculations and display the results    
