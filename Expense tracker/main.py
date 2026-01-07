def get_amount() -> float:
    while True:
        raw = input("introduce el importe del gasto: ")

        try:
            amount = float(raw)
            if amount <= 0:
                print("El importe debe ser mayor que 0.")
                continue
            return amount
        except ValueError:
            print("Introduce un número válido.")


def get_category() -> str:
    category = input("Introduce la categoría del gasto: ").strip()

    if not category:
        return "unknown"
    return category

def main() -> None:
    print("=== Expense Tracker v0.2 ===")

    expenses = []

    amount = get_amount()
    category = get_category()

    expense = {
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)

    print("\nGasto añadido correctamente")
    print(expense)

    print("\nResumen actual:")
    for e in expenses:
        print(f"- {e['category']}: {e['amount']} €")

if __name__ == "__main__":
    main()
