# Brady Buttrey, Matthew Krivitskiy, Carlos Osorio, Luis Valderrama
# Professor Bill Farmer
# INST 326: Final Project
# 12/15/2022


import sys
import argparse
import pandas as pd
import re
import unittest
'''
Using this software, users can input their desired laptop components and if two of more of the components match from an individual laptop, the laptop ID# along with the matching specs will be returned for the user.

'''


def SearchOption():  # Matthew
    '''This function will ask the user if they want to search by specs or price alone.

    args:
        searchBy(str): The user will input how they want to search (by specs or price)

    returns:
        searchBy(str): The users input of how they want to search

    '''

    # asks the user how the want to search for a laptop
    searchBy = input(
        "Would you like to search by specs or by price? (Please enter 'specs' or 'price)\n")

    # ensures that a valid response what inputted
    if searchBy not in ["Specs", "specs", "Price", "price"]:
        # if not, it raises a ValueError
        raise ValueError("You must enter a valid response")
    return searchBy


def price_display(laptop_data, order):  # Carlos
    '''this method checks the users display desire and sorts the objects in ascending or descending

    args:
        reverse(bool): remains False if the user wants to display in ascending order, turns True if the user picks descending
        x: The sorted laptop data

    returns:
        x    
    '''
    reverse = False
    if order in ["d", "D"]:
        reverse = True

    x = sorted(laptop_data, key=lambda x: x.price, reverse=reverse)

    return x


def get_price_range():  # Matthews
    '''This function will collect the users price and convert it to INR currency

    args:
        dollar_range(int): sets the default range of the price 
        dollar_amount(str): takes the users price as a string
        Price(float): runs the conversion on dollar_amount to change from USD to INR

    returns:
        Price(float): the converted dollar_amount the user wants to search for. 

    '''

    dollar_range = 200
    dollar_amount = input("What price would you like to search around?: ")
    Price = float(dollar_amount) / .0121

    print(
        f"Searching for Laptops around {Price} dollars and diplaying Laptops within +-{dollar_range}")
    return Price


def price_loop(laptop_data, Price):  # Brady and luis
    '''This method find all the laptops within the given price range, creates objects of those laptops, and appends them to a list.

    args: 
        price_laptops(list): the list to hold all Laptop objects
        object(Obj): Laptop objects created


    '''
    price_laptops = []
    for row in laptop_data.iterrows():
        # .between(Price - 200, Price + 200, include=True):
        if row[1]["Price"] > Price - 200 and row[1]["Price"] < Price + 200:
            object = Laptop(row[1]["ID"], row[1]["Company"], row[1]["TypeName"], row[1]["Inches"], row[1]["ScreenResolution"], row[1]["Cpu"],
                            row[1]["Ram"], row[1]["Memory"], row[1]["Gpu"], row[1]["OpSys"], row[1]["Weight"], row[1]["Price"])
            price_laptops.append(object)

    return price_laptops


def price_option():  # carlos
    '''This fuction with ask the user how they want the laptops displayed (ascending or decending)

    display_choice(str): Takes the users input on what order they want the laptops displayed

    Raises:
        ValueError: if user input is not within the list of answers 

    returns:
        Display choice(str): takes the users input on what order they want the laptops displayed 

    '''
    display_choice = input(
        "Would you like it displayed in descending or , or ascending order? \nPlease only enter 'd' for descending or 'a' for ascending: ")

    # if choice is not within the list of correct answers
    if display_choice not in ["d", "D", "a", "A"]:
        # raise an error
        raise ValueError(
            "You must enter either 'd', 'D', 'a', or 'A'. Please restart and try again")
    return display_choice


def write_to_file(laptop_data):  # luis
    '''this method writes the laptop objects to the sorted.txt file

    '''
    with open("sorted.txt", "w") as f:
        for i in laptop_data:
            f.write("ID:" + str(i.id) + " " + i.company + " " + i.typeName + " " + str(i.inches) + " " + i.resolution + " " + i.cpu + " " +
                    i.ram + " " + i.memory + " " + i.gpu + " " + i.opSys + " " + i.weight + " " + str(i.price) + "\n")


class Laptop():  # Brady
    '''this class will be the laptop objects created from matching laptops

    attributes:
        id(int): the laptop id
        company(str): the laptop company 
        typeName(str): the type of laptop
        inches(int): the inches of the laptop 
        resolution(str): the resolution of the laptop
        cpu(str): the cpu of the laptop 
        ram(str): the ram of the laptop
        memory(str): the amount of memory in the laptop
        gpu(Str): the gpu of the laptop
        opSys(str): the operating system of the laptop 
        weight(str): the weight of the laptop
        price(str): the price of the laptop

    '''

    def __init__(self, id, company, typeName, inches, resolution, cpu, ram, memory, gpu, opSys, weight, price):  # Brady
        '''initializes a Laptop object

        attributes:
        id(int): the laptop id
        company(str): the laptop company 
        typeName(str): the type of laptop
        inches(int): the inches of the laptop 
        resolution(str): the resolution of the laptop
        cpu(str): the cpu of the laptop 
        ram(str): the ram of the laptop
        memory(str): the amount of memory in the laptop
        gpu(Str): the gpu of the laptop
        opSys(str): the operating system of the laptop 
        weight(str): the weight of the laptop
        price(str): the price of the laptop

        '''
        self.id = id
        self.company = company
        self.typeName = typeName
        self.inches = inches
        self.resolution = resolution
        self.cpu = cpu
        self.ram = ram
        self.memory = memory
        self.gpu = gpu
        self.opSys = opSys
        self.weight = weight
        self.price = price


def userDesires(laptop_data):  # Carlos
    '''This function will take the user desire/inputed components and make them key value pairs.
Args:
    UserCompany(str): users desired company
    UserTypeName (str): users desired laptop type
    UserInches(str): users desired screen length in inches
    UserResolution(str):Users desired screen resolution
    UserCpu (str): users desired Cpu
    UserRam(str): users desired amount of RAM
    UserMemory(str):users desired storage memory amount
    UserGpu(str):users desired GPU
    UserOpSys(str): Users desired operating system
    UserWeight(str): Users desired laptop weight
    Userprice(str): Users desired price

    specs(dictionary): key value pairs of components

returns: 
    specs(dictionary): a key value pairs of components 

    '''

    # empty dictionary to be added to
    specs = {}

    # takes the company input from the user
    UserCompany = input(
        "What company are you searching for? (if none say 'NA'): ")
    # checks if the company is an actual value or if user puts na
    if UserCompany not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual company
        specs["Company"] = UserCompany

    # takes the Type of laptop from the users input
    UserTypeName = input("What type are you looking for? (if none say 'NA'): ")

    # checks if the type is a an actual type, if not ignore it
    if UserTypeName not in ["NA", "na", 'None', 'none']:
        # creates key value pair in specs if its an actual type
        specs["TypeName"] = UserTypeName

    # takes the desired inches from the users input
    UserInches = input(
        "How many Inches would you like the screen? (if none say 'NA'): ")

    # checks if the inches is a an actual input, if not ignore it
    if UserInches not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["Inches"] = UserInches

    # takes the desired resolution from the users input
    UserResolution = input(
        "What Screen resolution are you looking for? (if none say 'NA'): ")
    # checks if the resolution is a an actual input, if not ignore it
    if UserResolution not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["Resolution"] = UserResolution

    # takes the desired Cpu from the users input
    UserCpu = input("What cpu are you looking for? (if none say 'NA'): ")

    # checks if the cpu is a an actual input, if not ignore it
    if UserCpu not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["Cpu"] = UserCpu

    # takes the desired Ram from the users input
    UserRam = input("How much Ram are you looking for? (if none say 'NA'): ")

    # checks if the ram is a an actual input, if not ignore it
    if UserRam not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["Ram"] = UserRam

    # takes the desired Memory from the users input
    UserMemory = input(
        "How much storage memory(please specify amount and type SSD, HDD, or flash storage): ")

    # checks if the memory is a an actual input, if not ignore it
    if UserMemory not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["Memory"] = UserMemory

    # takes the desired Gpu from the users input
    UserGpu = input("What Gpu are you looking for? (if none say 'NA'): ")

    # checks if the gpu is a an actual input, if not ignore it
    if UserGpu not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["Gpu"] = UserGpu

    # takes the desired Operating system from the users input
    UserOpSys = input(
        "What Operating System are you looking for? (if none say 'NA'): ")

    # checks if the operating system is a an actual input, if not ignore it
    if UserOpSys not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["OpSys"] = UserOpSys

    # takes the desired laptop weight from the users input
    UserWeight = input("What Weight are you looking for? (if none say 'NA'): ")

    # checks if the weight is a an actual input, if not ignore it
    if UserWeight not in ["NA", "na", 'None', 'none']:
        # creates a key value pair in specs if its an actual input
        specs["Weight"] = UserWeight

    # takes the desired laptop price from the users input
    myPrice = input(
        "What Price are you looking around? (if none say 'NA'): ")
    # checks if price is an actual input and not na
    if myPrice not in ["NA", "na", 'None', 'none']:
        # converts the price from USD to INR (what it is in the df)
        UserPrice = float(myPrice) / .0121
        # creates a key value pair in specs
        specs["Price"] = UserPrice

    return specs


def specs_filter(specs, laptop_data):  # Brady
    '''This function will check if at least two or more components are matching the users desires, create Laptop objects, and append them to a list.

    args:
        specs(dictionary): of search components 
        laptop_data(df): dataframe 


    returns: 
        specs_laptops(list): list of laptop objects 

    '''

    specs_laptops = []
    for row in laptop_data.iterrows():
        spec_count = 0
        for spec in specs:
            match = False
            if spec == "Price":
                Price = specs[spec]
                if row[1]["Price"] > Price - 200 and row[1]["Price"] < Price + 200:
                    match = True

            if specs[spec] == row[1][spec]:
                match = True
            if match:
                spec_count += 1
                if spec_count >= 2:
                    object = Laptop(row[1]["ID"], row[1]["Company"], row[1]["TypeName"], row[1]["Inches"], row[1]["ScreenResolution"], row[1]["Cpu"],
                                    row[1]["Ram"], row[1]["Memory"], row[1]["Gpu"], row[1]["OpSys"], row[1]["Weight"], row[1]["Price"])
                    specs_laptops.append(object)
                    break

    return specs_laptops


def main(filename):  # Brady & Carlos
    '''
    openes and reads into the laptop_data file 
    '''
    laptop_data = pd.read_csv(filename)
    searchBy = SearchOption()
    if searchBy in ['Price', 'price']:
        price = get_price_range()
        filter_data = price_loop(laptop_data, price)
    elif searchBy in ["Specs", 'specs']:
        specs = userDesires(laptop_data)
        filter_data = specs_filter(specs, laptop_data)

    order = price_option()
    sorted_data = price_display(filter_data, order)

    write_to_file(sorted_data)


if __name__ == "__main__":
    main('laptop_data.csv')
