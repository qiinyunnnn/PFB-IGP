
PROFIT AND LOSS
from pathlib import Path
import csv
fp = Path.cwd()/'csv_reports'/"Profit_And_Loss.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    Profit_And_Loss = []
    for row in reader:
        Profit_And_Loss.append([row[0],row[4]])

def profit_loss():
    '''
    This function is for calculating the difference in the net profit column and prints out the day and amount the highest increment occurs
    '''
    # creates a for loop that iterates over a sequence of numbers starting from 1 up to the length of the "Profit_And_Loss" dataset
    for day in range(1, len(Profit_And_Loss)): 
         # retrieves the profit value for the current day and converts it to an integer, and assign it to the variable current_day_profit
        current_day_profit = int(Profit_And_Loss[day][1])
        # retrieves the profit value for the previous day and converts it to an integer, and assign it to the variable prev_day_profit
        prev_day_profit = int(Profit_And_Loss[day-1][1])
        # The calculated "difference" variable will store the profit differences between each consecutive day, representing how much profit increased or decreased from one day to the next
        difference = prev_day_profit - current_day_profit

        if difference > 0:
            print(f"[PROFIT DEFICIT] DAY: {Profit_And_Loss[day][0]}, AMOUNT: USD{difference}") # Prints out the day and the amount of difference 

# Call the function
profit_loss()










MAIN
# from pathlib import Path
# from overheads import find_highest_overhead
# from cash_on_hand import cash_on_hand
# from profit_loss import profit_loss
# main= [find_highest_overhead(), cash_on_hand(),profit_loss()]

# import cash_on_hand
# import overheads
# import profit_loss
# result = cash_on_hand
# print(result)

# fp = Path.cwd()/"summary_report.txt"
# with open("summary_report.txt","w" ) as file:
#     result=str(main())
#     file.write("{result}")


from pathlib import Path
import csv
def main():
    from overheads import find_highest_overhead
    from cash_on_hand import cash_on_hand
    from profit_loss import profit_loss
    return 
main()


# fp = Path.cwd()/"summary_report.txt"
# with fp.open(mode="w", encoding="UTF-8", newline="") as file:
#     file.write(main())
        
with open("summary_report.txt","w" ) as file:
    file.write(f"{main()}")

