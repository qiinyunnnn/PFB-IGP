
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

