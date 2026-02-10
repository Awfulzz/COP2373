def get_ticket_request(remaining_tickets):
    '''
    Prompts the user to enter the number of tickets they want to buy.
    Repeats until a valid request is entered.
    '''

    requested = 0

    # Loop until the user enters a valid number
    while requested < 1 or requested > 4 or requested > remaining_tickets:
        requested = int(input('How many tickets would you like to buy (1-4)? '))

        # Check if the request is invalid
        if requested < 1 or requested > 4 or requested > remaining_tickets:
            print('Invalid request. Please try again.')

    # Return a valid ticket request
    return requested


def sell_tickets():
    '''
    Controls the ticket selling process.
    Continues until all tickets are sold.
    '''

    total_tickets = 10
    buyers = 0  # accumulator

    # Loop until no tickets remain
    while total_tickets > 0:
        print('Tickets remaining:', total_tickets)

        # Get a valid ticket request
        tickets_bought = get_ticket_request(total_tickets)

        # Subtract tickets and count buyer
        total_tickets -= tickets_bought
        buyers += 1

    # Display final results after loop ends
    print('All tickets have been sold.')
    print('Total number of buyers:', buyers)


# Start the program
sell_tickets()