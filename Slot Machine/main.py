def spin_row():
    symbols = ['🍒', '🍉', '🍊', '🔔', '⭐' ]

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100
    print("**************************")
    print("Welcome to python Slots")
    print("Symbols:🍒 🍉 🍊 🔔 ⭐ ")
    print("**************************")

    while balance > 0:
        print(f"Current balance: {balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet = int(bet)

        if bet > balance:
            print("insufficent funds")
            continue
        
        if bet <= 0:
            print("bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)


if __name__ == '__main__':
    main()

