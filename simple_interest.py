##
# Program Name: interest_rate.py
# Program Description:
#   This is a small program to calculate the interest based on user input.
#
#   This program takes user input of principal, annual interest rate,
#   number of compound per year and years to earn interest.
#   Then it uses a formula to calculate the total amount and interest earned.
#
#   The program keeps asking user input till user type in 0 to quit the
#   program.
# @Author:   Yun Mao
# @Date:     6/30/2021
#

# Initilize variable

def interest_rate() :

    # Use a while loop to ask user input
    p = 0.0
    while p >= 0 :
    
        p = float(input("Enter the starting principal, <=0 to quit: "))
        # Loop break condition
        if p <= 0 :
            print("Exiting Simple Interest program ...")
            break
        else :
            r = float(input("Enter the annual interest rate: "))
            n = float(input("How many times per year the interest compounded? "))
            t = float(input("For how many years will the account earn interest? "))

  
        # To calculate total amount and interest earned:
            total = p * (1 + float(r / 100) / n) ** (n * t)
        interest = total - p
        print("At the end of ", format(t, ',.1f'), \
              " years you will have $", format(total, ',.2f'), \
              " with interest earned $ ", format(interest, ',.2f'), \
              end="")
        print()
   

if __name__ == "__interest_rate__" :
    interest_rate()
