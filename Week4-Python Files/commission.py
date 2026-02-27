# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
# keep_going.lower() == 'y'
while keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the % commission rate: '))
    

            
    # Calculate the commission.
    commission = sales * comm_rate/100
    if sales > 5000:
        commission += 50

    # Display the commission.
    print('The commission is £', \
            format(commission, '.2f'),sep='')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' + \
                        'commission (Enter y for yes): ').lower()

# end of while loop

print('OK - goodbye.')



