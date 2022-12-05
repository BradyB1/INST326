"""A template for a python script deliverable for INST326.

Driver: Brady Buttrey
Navigator: Mosies Hernandez 
Assignment: Template INST326
Date: 12/3/2022

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


import re


def parse_name(text: str):
    '''this function matches the first and last name in the txt file using regular expressions

    args:
        text(str): a single line of the txt file 
    returns:
        Tuple containing first and last name 
    '''
    # uses regex to search the file for the matching expression
    first_name = re.search(r"^\w+", text).group()
    # uses regex to search the file for the matching expression
    last_name = re.search(r"\w{3,10}(?=\s\d)", text).group()
    # returns first and last name as a tuple
    return (first_name, last_name)


def parse_address(text: str):
    '''This function matches the street, city and state in the txt file using regex

    args: 
        Text(str): a single line of the txt file 

    returns: 
        Address object containing street, city, and state 
    '''

    # uses regex to search the file for the street
    street = re.search(
        r"(\d+\s*)\w+\s\w+[ Drive]*[Road]*[Avenue]*[Street]*(?=\s)", text).group()
    # uses regex to search the file for the city
    city = re.search(r"\w+ (?=[A-Z]{2})", text).group()
    # uses regex to search the file for the state
    state = re.search(r"[A-Z]{2}", text).group()

    # returns the address as an object
    return Address(street, city, state)


def parse_email(text: str):
    '''This function matches the email in the txt file using regex

    args: test(str): a single line of the txt file 

    returns:
        email(str)
    '''
    # uses regex to search the file for the email
    email = re.search(r"\S+@\S+\.\S+", text).group()
    # returns email
    return email


class Address():
    '''
    This is a class for address

    attributes:     
        street(str): Employees street
        city(str): employees city 
        state(str): employees state
    '''

    def __init__(self, street, city, state):
        '''initializes the address class

    attributes:     
        street(str): Emplyoees street
        city(str): Employees city. Using .rstrip() to trim the whitespace from the end of the city 
        state(str): Employees state 
        '''
        self.street = street
        self.city = city.rstrip()
        self.state = state


class Employee():
    '''
    A class for creating employee objects    

    Attributes:
        first_name(str): The first name pulled from parse_name
        last_name(str): The last name pulled from parse_name 
        address (str) : the address pulled from parse_address
        email(str): the address pulled from parse_email 
    '''
    # if prof changes gradescope, change parameters to just (self, text)

    def __init__(self, first_name, last_name, address, email):
        '''
        initializes Employee object 

        args: 
        first_name(str): The first name pulled from parse_name
        last_name(str): The last name pulled from parse_name 
        address (str) : the address pulled from parse_address
        email(str): the address pulled from parse_email 

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email

        # if the prof changes
        # self.first_name = parse_name(i)[0]
        # self.last_name = parse_name(i)[1]
        # self.address = parse_address(i)
        # self.email = parse_email(i)


def main(path):
    '''
    In this function we open the file path and parse for the required strings using regex, add them to an employee list.

    args: 
        Path:The file name 
        first_name(str): The first name pulled from parse_name
        last_name(str): The last name pulled from parse_name 
        address (str) : the address pulled from parse_address
        email(str): the address pulled from parse_email 
        add_emp(object): add_emp becomes the employee object 
        employee_list(list): had add_emp appended to it in order to create a list of employees

    returns: employee_list(list): the list of employees 

    '''
    employee_list = []
    # opens the file path and parses for the matching expressions
    with open(path, "r") as f:
        for i in f:
            # if prof changes delete the following four lines
            first_name = parse_name(i)[0]
            last_name = parse_name(i)[1]
            address = parse_address(i)
            email = parse_email(i)

            # if prof changes just do Employee(i)
            # sets add_emp equal to employee objects
            add_emp = Employee(first_name, last_name, address, email)
            # appends employee objects to list
            employee_list.append(add_emp)
    # closes the file
    f.close()

    # for loop to print employees name address and email
    for emps in employee_list:
        print(f"First Name: {emps.first_name}")
        print(f"Last name: {emps.last_name}")
        print(f"Street: {emps.address.street}")
        print(f"City: {emps.address.city}")
        print(f"State: {emps.address.state}")
        print(f"Email: {emps.email}")
    # returns the employee list
    return employee_list


if __name__ == "__main__":
    x = main("people.txt")
    print(x)
