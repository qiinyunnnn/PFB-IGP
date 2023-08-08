from pathlib import Path
import csv
fp = Path.cwd()/'csv_reports'/"Cash_On_Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    Cash_On_Hand = []
    for row in reader:
        Cash_On_Hand.append([row[0],row[1]])
# print(Cash_On_Hand)

def cash_on_hand_function():
    '''
    This function is for calculating the difference in Cash-on-hand and prints out the day and amount the highest increment occurs
    '''
    cash_deficit = [] # Creates an empty list to store cash deficit data 
    # creates a loop that iterates over a sequence of numbers starting from 1 up to the length of the "Cash_On_Hand" dataset
    for day in range(1, len(Cash_On_Hand)):
        current_day_cash = int(Cash_On_Hand[day][1]) # Finds the current day's amount 
        prev_day_cash = int(Cash_On_Hand[day-1][1]) # Finds the previous day's amount
        difference = prev_day_cash - current_day_cash # Calculates the difference 

        if difference > 0: # If the difference is >0, meaning there is a cash deficit
            cash_deficit.append(f"[CASH DEFICIT] DAY: {Cash_On_Hand[day][0]}, AMOUNT: USD{difference}")
    print(cash_deficit) # Print list to check if the items in the list were printed out correctly 
    return cash_deficit # Returns the cash_deficit list to the function

cash_on_hand_function() # Call the function to perform the calculations and display the results 

