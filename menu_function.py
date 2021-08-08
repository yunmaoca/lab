##
# Program Name: menu_function.py
# Program Description:
#   This is a program to allow user to choose an option from
#   a menu and execute the program accordingly.
#   The menu has three options:
#   1.  Calculate Simple Interest
#   2.  Calculate Mortgage Payment
#   99. Quit the program
#
#   The first part of the program to print class name, coder name, lab name
#   and the current time when the program is run.
#
#   The second part of the program uses a "main" function and display a menu
#   with the options listed above. This code uses a while loop to take user
#   input and execute accordingly.
#   
#   This program imports a local python program called "simple_interest". When
#   user chooses option 1, function simple_interest.interest_rate() is called
#   and executed.
#
#   Option 2 is defined in a local function called mortgage(), it uses a while
#   loop to take user input.  It uses a formula to calculate the total amount
#   paid for the loan and total interest  of the load to be paid. It prints out
#   the details of the loan and its interest. When user uses 0 as the load amount,
#   it breaks the loop and exits.
#  
#   When user chooses option 3, it quits the program.
#   When user type in a number other than 1, 2 and 99, the program prints out
#   an error message and asks user to select the menu again.
#
# @Author:   Yun Mao
# @Date:     7/5/2021
#

from datetime import datetime

# print name, lab name and current time
name = "CNET-142: Yun Mao - "
lab_name = "Lab 4: Menu Function"
print (name, lab_name)

currentTime = datetime.now()
ctime_str = str(currentTime)
timestampStr = currentTime.strftime("%Y-%m-%d %I:%M:%S%p")
print("{:16}".format(timestampStr))

print("\n")

import simple_interest

def main() :
  
    print("-" * 30)
    print ("1\t Calculate Simple Interest")
    print ("2\t Calculate Mortgage Payment")
    print ("99\t Quit the program")
    print("-" * 30)
    print()

    choice = input("Select one of the command number above: ")
    while (choice != '99') :
        if (choice == '1') :
            simple_interest.interest_rate()
            break
        elif (choice == '2') :
            mortgage()
            break
        else :
            print ("Error: command not recognized")
            choice = input("Select one of the command number above: ")
    print ("Have a nice day!..")
         
def  mortgage() :

    # Initilize variable
    loanAmount = 0.0
    interestRate = 0.0
    loanTerm = 0.0


    # Use a while loop to ask user input
    while loanAmount >= 0 :
    
        loanAmount = float(input("Enter the load amount, 0 to quit: "))
        # Loop break condition
        if loanAmount == 0 :
            print("Program exiting ...")
            break
        else :
            interestRate = float(input("Enter the loan interest rate %: "))
            loanTerm = float(input("Enter the loan term (number of years): "))

        # To calculate total amount and interest earned:
        monthlyRate = (interestRate / 100) / 12
        numPayments = loanTerm * 12
        monthlyPayment = loanAmount * monthlyRate \
        * pow((1 + monthlyRate), numPayments) \
        / (pow((1 + monthlyRate),numPayments) - 1)
        totalPayment = monthlyPayment * (loanTerm * 12)
        interestPaid = totalPayment - loanAmount

        
        print('For the loan amount of $', format(loanAmount, ",.2f"), \
              ' for ', format(loanTerm, ",.0f"),\
              ' years with interest rate of ', format(interestRate, ",.2f"), '%', sep='')
        print('The monthly payment is $', format(monthlyPayment, ',.2f'),sep='')
        print('Total amount paid for this loan is $', format(totalPayment, ',.2f'),sep='') 
        print('Total interest paid for this loan is $', format(interestPaid, ',.2f'),sep='')        
        
        print()
   

if __name__ == "__main__" :
    main()


