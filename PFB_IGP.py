
from cash_on_hand import cash_on_hand_function
from overheads import find_highest_overhead
from profit_loss import profit_loss_function

def main ():
    Cash_On_Hand = cash_on_hand_function() # Assigns each function to a variable 
    Overheads = find_highest_overhead()
    Profit_Loss = profit_loss_function()
    cash_deficit_lines = "" # Formats the cash_on_hand_function to write each Day and Amount pair to it's own line 
    for cash_deficit in Cash_On_Hand:
        cash_deficit_lines += cash_deficit + "\n"
    profit_loss_lines = "" # Formats the profit_loss_function to write each Day and Amount pair to it's own line 
    for profit_deficit in Profit_Loss:
         profit_loss_lines += profit_deficit + "\n"
    output = f"[HIGHEST OVERHEAD] {Overheads[0][0].upper()}: {Overheads[0][1]}%\n" # Creates output variable to store the different functions 
    output += f"{cash_deficit_lines}"
    output += f"{profit_loss_lines}"
    with open('output.txt', 'w') as file:
            file.write(output)  # Writes the result to a text file 

main() # Calls the function 

