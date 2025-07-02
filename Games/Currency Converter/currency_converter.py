def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Please enter a positive number")

def get_currency(label):
    currencies = ('INR', 'USD', 'EUR', 'KWD')
    while True:
        currency = input(f"Enter the {label} currency to convert: ").upper()
        if currency not in currencies:
            print("Please enter a valid currency.")
        else:
            return currency

def convert(amount,source_currency,target_currency):
    exchange_rates = {
        'INR' : {'USD' : 0.012, 'EUR' : 0.0099, 'KWD' : 0.0036 },
        'USD' : {'INR' : 85.60, 'EUR' : 0.85, 'KWD' : 0.31 },
        'EUR' : {'INR' : 100.85, 'USD' : 1.18, 'KWD' : 0.85 },
        'KWD' : {'INR' : 280.46, 'USD' : 3.28, 'EUR' : 2.78},
    }

    if source_currency == target_currency:
        return amount

    return amount*exchange_rates[source_currency][target_currency]


def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    history = []
    while True:
        target_currency = get_currency('Target')
        converted_amount = convert(amount,source_currency,target_currency)
        print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}\n")

        history.append(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

        choice = input("Do you want to enter another target currency(y/n): ").lower()
        if choice == 'n':
            print("Your conversion history")
            for record in history:
                print(record)
            print("\nThank you")
            break

if __name__ == '__main__':
    main()
