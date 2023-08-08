#profit and loss 
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
    difference_in_net_profit = []
    # creates a for loop that iterates over a sequence of numbers starting from 1 up to the length of the "Profit_And_Loss" dataset
    for day in range(1, len(Profit_And_Loss)): 
         # retrieves the profit value for the current day and converts it to an integer, and assign it to the variable current_day_profit
        current_day_profit = int(Profit_And_Loss[day][1])
        # retrieves the profit value for the previous day and converts it to an integer, and assign it to the variable prev_day_profit
        prev_day_profit = int(Profit_And_Loss[day-1][1])
        # The calculated "difference" variable will store the profit differences between each consecutive day, representing how much profit increased or decreased from one day to the next
        difference = prev_day_profit - current_day_profit

        if difference > 0:
           difference_in_net_profit.append(f"[PROFIT DEFICIT] DAY: {Profit_And_Loss[day][0]}, AMOUNT: USD{difference}")
    return difference_in_net_profit
# Call the function
profit_loss_function()









MAIN
from cash_on_hand import cash_on_hand_function
from overheads import find_highest_overhead
from profit_loss import profit_loss_function

def main ():
    Cash_On_Hand = cash_on_hand_function()
    Overheads = find_highest_overhead()
    Profit_Loss = profit_loss_function()
    
    print(Cash_On_Hand)
    print(Overheads)
    print(Profit_Loss)

    cash_deficit_lines = ""
    for deficit in Cash_On_Hand:
        cash_deficit_lines += deficit + "\n"

    profit_loss_lines = ""
    for profit in Profit_Loss:
         profit_loss_lines += profit + "\n"
         

    output = f"{cash_deficit_lines}"
    output += f"[HIGHEST OVERHEAD] {Overheads[0][0].upper()}: {Overheads[0][1]}%\n"
    output += f"{profit_loss_lines}"
    with open('output.txt', 'w') as file: # Writes the result to a text file 
            file.write(output)

main()

