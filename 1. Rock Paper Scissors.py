"""A template for a python script deliverable for INST326.
Driver: Brady Buttrey
Navigator: Yash Gupta
Assignment: Template INST326
Date: 9_7_22
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import sys
import argparse
def main(player1_name= input("Player1 please enter your name: "), player2_name= input("Player2 please enter your name: ")):
    ''' Takes in two parameters to get player names
        Later asks for players hand sign
        prints player hand signs
        runs determine winners check for winner/tie
    '''
    p1 = input(player1_name +" please enter your hand sign r, p, or s: ")
    p2 = input(player2_name +" please enter your hand sign r, p, or s: ")
    determine_winner(player1_name, player2_name)
    print("Player 1 chose: " + p1)
    print("Player 2 chose: " + p2)
    if determine_winner(p1,p2) =="Tie!":
        print("Tie!")
    elif determine_winner(p1,p2) == "Invalid response":
        print("Please try again and enter a valid response. (r, p, or s)")
    elif determine_winner(p1,p2) == "Player1":
        print(player1_name+ " wins!")
    else:
        print(player2_name+ " wins!")

    #add if elif to check player1, player2, tie
    
    


def determine_winner(p1, p2):
    #fix to p1, p2
    #simplify if elif statement to barebone checks 
    ''' Takes to parameters and checks for a winner through an if/elif sequence'''
    if p1 == "r" and p2 == "r":
        return "Tie!"
    elif p1 == "r" and p2 == 's':
        return "Player1"
    elif p1 == "r" and p2 == 'p':
        return "Player2"
    elif p1 == "s" and p2 == 's':
        return "Tie!"
    elif p1 == "s" and p2 == 'p':
        return "Player1"
    elif p1 == "s" and p2 == 'r':
        return "Player2"
    elif p1 == "p" and p2 == 'p':
        return "Tie!"
    elif p1 == "p" and p2 == 'r':
        return "Player1"
    elif p1 == "p" and p2 == 's':
        return "Player2"
    else:
        return "Invalid response"

#main()


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as 
arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations commence. 
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('player1_name', type=str, help='Please enter player1 name.')
    parser.add_argument('player2_name', type=str, default=12, help='Please enter player2 name.')  
    
    
    #NEED PROF TO LOOK AT, NOT UNDER STANDING 
    args = parser.parse_args(p1, p2) #We need to parse the list of command line arguments using this object.
    return args

if __name__ == "__main__":
    main()
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?
    #It the script is being run as a module, the block of code under this will not be executed.
    #If the script is being run natively, the block of code below this will be executed.
    
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
    
    main(arguments.player1_name, player2_name)

