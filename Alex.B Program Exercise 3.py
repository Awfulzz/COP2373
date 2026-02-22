'''
Program Name: Monthly Expense Analyzer
Description:
This program asks the user to enter their monthly expenses
(type and amount). It then uses the reduce() function to
calculate the total expense, highest expense, and lowest expense.
'''

from functools import reduce


def get_expenses():
    '''
    Prompts the user to enter expense types and amounts.
    Returns a list of dictionaries containing expense data.
    '''

    expenses = []

    print('Enter your monthly expenses.')
    print('Type "done" when finished.\n')

    while True:

        expense_type = input('Enter expense type: ')

        if expense_type.lower() == 'done':
            break

        try:
            amount = float(input('Enter expense amount: $'))

            if amount < 0:
                print('Amount cannot be negative. Try again.\n')
                continue

            expenses.append({'type': expense_type, 'amount': amount})

        except ValueError:
            print('Invalid amount. Please enter a number.\n')

    return expenses


def calculate_total(expenses):
    '''
    Uses reduce() to calculate total expense amount.
    Returns the total.
    '''

    total = reduce(lambda acc, expense: acc + expense['amount'], expenses, 0)
    return total


def calculate_highest(expenses):
    '''
    Uses reduce() to determine the highest expense.
    Returns the dictionary containing the highest expense.
    '''

    highest = reduce(
        lambda acc, expense: expense if expense['amount'] > acc['amount'] else acc,
        expenses
    )

    return highest


def calculate_lowest(expenses):
    '''
    Uses reduce() to determine the lowest expense.
    Returns the dictionary containing the lowest expense.
    '''

    lowest = reduce(
        lambda acc, expense: expense if expense['amount'] < acc['amount'] else acc,
        expenses
    )

    return lowest


def display_results(expenses):
    '''
    Displays total, highest, and lowest expense information.
    '''

    if not expenses:
        print('\nNo expenses were entered.')
        return

    total = calculate_total(expenses)
    highest = calculate_highest(expenses)
    lowest = calculate_lowest(expenses)

    print('\n----- Expense Summary -----')
    print(f'Total Expenses: ${total:.2f}')
    print(f'Highest Expense: {highest["type"]} - ${highest["amount"]:.2f}')
    print(f'Lowest Expense: {lowest["type"]} - ${lowest["amount"]:.2f}')


def main():
    '''
    Main function that runs the program.
    '''

    expenses = get_expenses()
    display_results(expenses)


if __name__ == '__main__':
    main()