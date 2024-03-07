#3 by 3 slot machine
#User only gets a line if he/she gets 3 in a row on the reels


import random
import time

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#Number of rows and columns in the slot machine
ROWS = 3
COLS = 3

#Symbols in each reel
symbol_count = {
    '7    ': 2,
    'BAR  ': 4,
    'APPLE': 6,
    'BELL ': 7
}

#Symbol's values
symbol_value = {
    '7    ': 5,
    'BAR  ': 4,
    'APPLE': 3,
    'BELL ': 2
}


#Calculating the winning amount
def check_win(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)
    return winnings, winning_line


#Output of the spin
def get_machine_spin_output(rows, cols, symbols):
    #Creating an all symbols list
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    #Generating random values inside of the columns
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


#Print the output of the columns that were randomly generated
def print_slot_machine_output(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end = ' | ')
                time.sleep(0.5)
            else:
                print(column[row], end = '')
                time.sleep(0.5)
        print()
    time.sleep(0.4)


#Collects user input about their deposit
def deposit():
    while True:
        amount = input("How much would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a deposit amount that is greater than 0.")
        else:
            print("Please enter a number.")
    return amount


#Collects number of lines the user wants to bet on
def number_of_lines():
    while True:
        lines = input(f"How many lines would you like to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


#Collects the amount the user wants to bet on each line
def bet_on_lines(balance):
    if balance <= 0:
        print("Insufficient balance.")
        print("Thank you for playing. PLAY AGAIN!!!")
        quit()
    while True:
        amount = input("How much would you like to bet on each line? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_BET and amount <= MAX_BET:
                break
            else:
                print(f"Betting amount must be within ₹{MIN_BET} - ₹{MAX_BET}")
        else:
            print("Please enter a number.")
    return amount


#Each round or spin
def round(balance):
    lines = number_of_lines()

    #Checking if betting amount is within the user's balance
    while True:
        bet = bet_on_lines(balance)
        total_bet = bet * lines
        if total_bet >balance:
            print(f"You do not have enough balance to bet that amount.\nBalance = ₹{balance}")
        else:
            break

    print (f"You are betting ₹{bet} on {lines} lines.\nTotal bet = ₹{total_bet}")

    print("SPINNING.....")
    slots = get_machine_spin_output(ROWS, COLS, symbol_count)
    print_slot_machine_output(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f'You won ₹{winnings}')
    if winnings != 0:
        print(f'You won on line numbers: ', *winning_lines)
    return winnings - total_bet


#If user wants to play again, we just run this main function again
def main():
    print("Welcome to the Text-based Slot Machine. LETS PLAY!!")
    balance = deposit()
    print_check_balance = balance

    while True:
        print(f"Current balance = ₹{balance}")
        spin = input("Press 'Enter' to play OR Press 'q/Q' to quit.")
        if spin == 'q' or spin == 'Q':
            break
        balance += round(balance)
    
    print(f"You exited with ₹{balance}")
    if balance >= print_check_balance:
        print(f"Profit made = ₹{balance-print_check_balance}")
    else:
        print(f"Loss = ₹{print_check_balance-balance}")
    print("Thank you for playing. PLAY AGAIN!!!")


main()