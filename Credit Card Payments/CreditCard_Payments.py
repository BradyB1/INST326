"""Perform credit card calculations."""
from argparse import ArgumentParser
import sys

def get_min_payment(balance, fees=0):
    '''
    calculates the minimum payment 
    
    args: 
        balance (int): the total balance left to pay 
        fees (int): Fees associated with credit card account. Default to 0
        b: is the balance (just used in the equation for min_payment) 
        f: fees (used in the equation for min_payment)
        m: the percent of the balance that needs to be paid (constant value of .02)
        min_payment: calculates the minimum payment
        
    returns: 
        (int) min_payment
    '''
    
    #set b = to balance 
    b = balance        
    #sets m = to constant value of .02
    m = .02
    #sets f= to fees
    f = fees

    #fomula for minimum payments 
    min_payment = ((b * m) + f)
    
    #if the minimum payment is less then 25, then set the minimum payment to 25
    if min_payment < 25: 
        min_payment = 25
    #returns min_payment 
    return min_payment
    

def interest_charged(balance, apr):
    '''
    Calculates the interest on payments 
    args: 
        balance(int): the balance of the credit card that has not been paid of yet
        apr(int): The annual apr (int between 0-100)
        a: apr 
        y: days in a year (365)
        b: balance set to b for the equation
        d: days in a year 
        i: calculates the interest charged
    
    returns
        i (float or int)
    '''
    #apr needs to be expressed as a floating point
    a = apr/100
    
    #number of days in a year 
    y = 365
    
    #account balance 
    b = balance
    
    #number of days in billing cycle = d
    d = 30


    #formula for interest stored as i 
    i = (a/y)*b*d
    #returns the interest to the function
    return i
    

#WORKING ON THIS
def remaining_payments(balance, apr, targetamount, credit_line= 5000, fees = 0):
    ''' Computes and returns the number of payments needed to pay off the credit card
    args: 
        balance (int): the balance of the credit card that has not been paid off 
        apr (int): the annual APR (int between 0-100)
        targetamount (int): the amount the user wants to pay per payment
        credit_line(int) : The max amount of balance that an account holder can keep in the account (defaults to 5000)
        fees (int): The amount of fees that will be charged in addition to minimum payment (dafaults to 0)
        x: Counter for number of payments to be made 
        count_25: count_25 represents the number of months that the balance remains over 25%
        count_50: count_50 represents the number of months that the balance remains over 50%
        count_75: count_75 represents the number of months that the balance remains over 75%
        payment: sets get_min_payments to a new variable for caluculate later
        TotalPayment: total amount to be paid, interest + payment (min_payment)
        Totalcounts: tuple of count_25,count_50,count_75, and x
        
        
    returns:
        Totalcounts: returns a tuple of count_25,count_50,count_75
    
    '''
    #this counter represents the number of payments to be made 
    x = 0
    #count_25 represents the number of months that the balance remains over 25%
    count_25= 0
    #count_50 represents the number of months that the balance remains over 50%
    count_50=0
    #count_75 represents the number of months that the balance remains over 75%
    count_75=0
    
    #loop to continue countings and keep interest adding 
    while balance > 0:
        #checks if target amount if not declared 
        if targetamount == None:
            #if target amount is not set then the payment is the minimum payment 
            payment = get_min_payment(balance, fees)
        
        else:
            #if the target amount if set, payments is set to that value 
            payment = targetamount
        
        #total payment takes the value of payment minus interest charged 
        TotalPayment = payment - interest_charged(balance, apr)
        #if total payment is less then 0 then the program quits 
        if TotalPayment < 0:
            print("The card balance cannot be paid off")
            quit()
        #keeps the Totalpayment substracting until paid off
        balance = balance - TotalPayment
        #adds 1 to x for every payment to be made 
        x+=1 
    
        #checks if the balance is 75% over the credit line
        if balance > credit_line*.75:
            #adds 1 to count_75 if it is over for that month
            count_75+=1
        #checks if the balance is 50% over the credit line
        if balance > credit_line*.50:
            #adds 1 to count_50 if it is over for that month
            count_50+=1
        #checks if the balance is 25% over the credit line
        if balance > credit_line*.25:
            #adds 1 to count_25 if it is over for that month
            count_25+=1
    
    #tuple to store counters 
    Totalcounts = (x,count_25,count_50,count_75)
    #returns counters to remaining_payments 
    return Totalcounts
            
            
            
    
    

    
    

    

def main(balance, apr,targetamount= None, credit_line = 5000, fees=0):
    ''' checks if targe amount it None or delcared, then ties all functions together to complete the displays 
    
    args: 
        TotalORemaining (tuple): sets remaining_payments function equal to TotalOfRemaining to make it easier to display counters stored in the tuple 
        pays_minimum (boolean): delcares pays_minium to False, if targetamount is not set then it is later made True
        
        
    returns: 
        total months spent over 25%, 50% and 75% of the creditline 
    
    '''
    #shows the user the recommened minimum payment 
    print(f"The recommened starting minimum payment is ${get_min_payment(balance, fees)}")
    #takes the tuple value from remaining_payments 
    TotalOfRemaining = remaining_payments(balance, apr, targetamount, credit_line, fees)
    #sets pays_minimum to false by default 
    pays_minimum = False
   #if the target amount isn't set they pay the minimum 
    if targetamount == None:
        #pays_minimum gets set to true 
        pays_minimum = True
    #otherwise is targetamount is less then the minimum payment, quit the program 
    elif targetamount < get_min_payment(balance, fees):
        print("Your target payment is less than the minimum payment for this credit card")
        quit()

    #if pays_minimum is true, display the number of payments it will take to pay off using min payment
    if pays_minimum == True:
         print(f"If you pay the minimum payments each month, you will pay off the credit card in {TotalOfRemaining[0]} payments")
    #if pays_minimum is false, dispaly the number of payments it will take ot pay off using targetamount 
    else:
         print(f"If you make payments of ${targetamount} , you will pay off the credit card in {TotalOfRemaining[0]} payments")
    
    
    #return string that tells user how many months they will be over 25%, 50%, and 75% of the credit line 
    return f"You will spend a total of {TotalOfRemaining[1]} months over 25% of the credit line \nYou will spend a total of {TotalOfRemaining[2]} months over 50% of the credit line\nYou will spend a total of {TotalOfRemaining[3]} months over 75% of the credit line"
    

    



    














def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = ArgumentParser()
    #changed 'balance_amount' to 'balance'
    parser.add_argument('balance', type = float, help = 'The total amount ofbalance left on the credit account')
    parser.add_argument('apr', type = int, help = 'The annual APR, should be an intbetween 1 and 100')
    parser.add_argument('credit_line', type = int, help = 'The maximum amount of balance allowed on the credit line.')
    parser.add_argument('--payment', type = int, default = None, help = 'The amount the user wants to pay per payment, should be a positive number')
    parser.add_argument('--fees', type = float, default = 0, help = 'The fees that are applied monthly.')
    # parse and validate arguments
    args = parser.parse_args(args_list)
    #changed balance_amount to balance
    if args.balance < 0:
        raise ValueError("balance amount must be positive")
    if not 0 <= args.apr <= 100:
        raise ValueError("APR must be between 0 and 100")
    if args.credit_line < 1:
        raise ValueError("credit line must be positive")
    if args.payment is not None and args.payment < 0:
        raise ValueError("number of payments per year must be positive")
    if args.fees < 0:
        raise ValueError("fees must be positive")
    return args

if __name__ == "__main__":
    try:
        arguments = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
        #changed balance_amount to balance 
    print(main(arguments.balance, arguments.apr, targetamount = arguments.payment, credit_line = arguments.credit_line, fees = arguments.fees))