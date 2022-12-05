""" 
Driver: Brady Buttrey
Navigator: Richmond  Yeboah
Assignment Exercise_3_Robots
Date: 11/7/2022
INST326-ESG1 Farmer Fall 2022
"""
import sys
import argparse
import csv

# Implement Battery, Robot, MedicalRobot, DriverRobot and main()
#   Partial code is provided for your convenience

###this is our parent class----------
class Battery(object):
    '''A standalone class that will be used by all classes to determine battery type 
    
    Args: 
        batterytype(str): the type of battery 
    
    
    '''
    def __init__(self, batterytype:str):
        '''initializes a Battery object 
        
        args:
            batterytype(str): see class documentation 
        
        '''
        self.batterytype = batterytype
        
    #this is the getter for batterytype
    @property
    def batterytype(self):
        '''getter for batterytype
        
        returns: 
            self.battertype (as private)
        
        '''
        return self.__batterytype
    
    
    #this is the getter for batterytype
    @batterytype.setter
    def batterytype(self, batterytype:str):
        '''
        this setter for battery type contains a check to ensure the batterytype is valid
        
        Raises: 
            valueerror if not a valid type 
        
        '''
        if Battery.isvalidbatterytype(batterytype):
            self.__batterytype = batterytype
        else:
            raise ValueError("Batterytype of robot must be one of Lithium-Ion, Nickel-Metal, or Lead-Acid")
    
    def __str__(self):
        return f"{self.batterytype}"
        
    
    @classmethod
    def isvalidbatterytype(cls, value):
        '''Class method to check if batterytypes value is one of the three correct options 
        
        Returns:
            True or False determined by the value of batterytype 
        '''
        if value in ['Lithium-Ion','Nickel-Metal-Hydride','Lead-Acid']:
            return True
        else: 
            return False
        

#parent class for all robots 
class Robot(object):  
    """A robot class that will be the base class (parent) for the rest of my robot types
        contains getters and setters for name, id, year, and battery 
        
    args: 
        name(str): name of robot 
        id(int): robot id 
        year(int): the year robot was made 
        battery(Battery): type of battery used in robot 
    
    
    """
    #version is a string variable 
    version = "0.1"
    
    def __init__(self, name:str, id:int, year:int, battery:Battery):
        '''initializes a Robot object
        
        args: 
        name(str): see class documentation  
        id(int): see class documentation 
        year(int): see class documentation 
        battery(Battery): see class documentation 
        
        '''
        self.name = name
        self.id = id 
        self.year = year
        self.battery = battery 
     
    ##Name below

    #name getter
    @property
    def name(self):
        '''getter for name 
        
        Returns:
            self.__name
        '''
        return self.__name
    
    #name setter
    @name.setter 

    def name(self, name):
        '''setter for name: checks to see if the robot name is valid  
        
        Raises:
            ValueError if not a valid name 
        '''
        if Robot.isvalidname(name):
            self.__name = name
        else: 
            raise ValueError("Name of robot must be 2 or more characters")
        
    ##ID below 

    #Id Getter
    @property
    def id(self):
        '''getter for id 
        
        Returns:
            self.__id
        
        '''
        return self.__id

    #ID Setter
    @id.setter
    def id(self,id):
        '''
        Setter for id
        args: 
            id(int): see class documentation 

        Raises:
            ValueError if id is not at least 2 digits long
        '''
        if int(id) < 10:
            raise ValueError("ID of Robot must be at least two digits.")
        else: 
            self.__id = int(id)

    ##Year Below

    # Year getter
    @property
    def year(self):
        '''getter for year 
        Returns:
            self.__year
        '''
        return self.__year

    #year setter
    @year.setter
    def year(self, year):
        '''setter for year
        args:
            year(int): see class documentation 
            
        Raises:
            ValueError if the year is not between 2000 and 2022
    
        '''
        if int(year) < 2000 or int(year) > 2022:
            raise ValueError("Year is not a valid year")
        else: 
            self.__year = int(year)

    ##BATTERY Below

    # Battery Getter
    @property
    def battery(self):
        '''getter for battery 
        Returns:
            self.__battery 
        '''
        return self.__battery
    #battery setter  
    @battery.setter

    def battery(self, battery):
        '''setter for battery
    
        args:
            battery(Battery): see class doc
        '''
        self.__battery = battery
        
    
    def talk(self):
        #won't let me put a doc string here 
        #allows the robot to talk 
        #returns: "I am a generic robot! Battery type:{self.__battery}"

       return f"I am a generic robot! Battery type:{self.__battery}"
        
        
    
    @classmethod
    def isvalidname(cls, value):
        '''Class method to check if users name length is greater than 1
        
        
        returns: True when name is valid, False when invalid 
        '''
        if len(value) > 1:
            return True
        else:
            return False

class MedicalRobot(Robot):
    """Creates and defines a medical robot Object
    Attributes:
        name(str): name of robot 
        id(int): robot id 
        year(int): the year robot was made 
        battery(Battery): type of battery used in robot 
        specialty(str): Robots specialty (can be 'General', 'Orthopedic', or 'Geriatric')
        
    """
    
    def __init__(self, name:str, id:int, year:int, battery:"Battery", specialty:str):
        super().__init__(name, id, year, battery) 
        

    @property 
    def specialty(self):
        return self.__specialty 

    @specialty.setter
    def specialty(self, specialty):
        
        '''setter for specialty. checks if specialty is a valid name from select options, if not it raises a valueerror.
        
        args:   
            Validspec(list): contains all valid specialities 
        
        Raises:
            ValueError when specialty is invalid 
        '''
        self.__specialty = specialty
        validspec = ['General', 'Orthopedic', 'Geriatric']
        if specialty in validspec:
            self.__specialty = specialty
        else:
            raise ValueError("Specialty must be one of General, Orthopedic, or Geriatric")
    
    
    def __str__(self):
        return f"{self.id} {self.name} Year:{self.year} {self.specialty}"
    
    def talk(self):
        '''allows medical robots to talk
        
            Returns:
            f"I am a medical robot! Battery type: {self.battery}"

        '''
        
        return f"I am a medical robot! Battery type:{self.battery}"

 
class DriverRobot(Robot):
    '''DriverRobot class, inherits from Robot class. 
    
    
    Attributes: 
        name(str): this is the name of the robot 
        id(int): represenets the id of the Robot 
        year(int): represents the year the Robot was made 
        battery(Battery): instance of the Battery class 
        licensestate(str): state for each driver robot license
        licenseid(str): licensesid for each Driver Robot
    '''
    def __init__(self, name:str, id:int, year:int, battery:"Battery", licensestate:str, licenseid:str):
        '''initializes a DriverRobot object 
        
        args: 
        name(str): see class documentation
        id(int): see class documentation
        year(int): see class documentation
        battery(Battery): see class documentation
        licensestate(str): see class documentation
        licensesid(str): see class documentation
        '''
        super().__init__(name, id, year, battery)
        self.licenseid = licenseid
        self.licensestate = licensestate
        
    # Need to have getter before setter for licensestate
    @property
    def licensestate(self):
        ''' getter for licensestate'''
        return self.__licensestate

    @licensestate.setter
    def licensestate(self, licensestate):
        '''setter for licensestate
        
        args:
            licensestate: holds the value of licenses staste 
            validstate(list): contains all valid states 
        
        Raises:
            valueerror if the state is not a valid state 
        '''
        validstate = ['PA','MD','VA','NY','NJ','DE']
        if licensestate not in validstate:
            raise ValueError('License must be in PA, MD, VA, NY, NJ, DE')

        else: 
            self.__licensestate = licensestate
    # Need to have getter before setter for licenseid
    @property
    def licenseid(self):
        '''getter for licenseid 
        '''
        return self.__licenseid 
    
    @licenseid.setter 
    def licenseid(self, licenseid):
        '''setter for licenseid
        
        args:
            licenseid(int): the licensesid of the robot
        raises valueerror if the id is not at least 5 characters long 
        '''
        if len(licenseid) != 5:
            raise ValueError("LicenseID must be 5 characters long")
        else: 
            self.__licenseid = licenseid

         
    def __str__(self):
        return f"{self.id} {self.name} Year:{self.year} State:{self.licensestate} LicenseId: {self.licenseid}"
    
    def talk(self):
        '''this function allows the robot object to talk 
        
        returns: string for robot talking
        '''
        return f"I am a driver robot! Battery type:{self.battery}"
'''  
 
'''
def main(filename:str):
    ''' opens and reads csv file and creates robot objects then adds them to the robots Array 
    args:
        robots(Array) : holds robot object after creation 
        
        

    returns: robots(Array of robots)
    '''
    
    robots =[] 
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        #for every line in the file, 
        for row in csv_reader:
            print(f'\tType:{row[0]} Name:{row[1]} ID:{row[2]}.')
            line_counter += 1
            battery = Battery(row[4])
            
            mybot = 0
            #if the row is "Robot"
            if row[0] == "Robot":
                #creates instance of robot 
                mybot = Robot(row[1], row[2], row[3], battery)
                #appends that instance to robots 
                robots.append(mybot)
                
            #if the row is "MedicalRobot"
            if row[0] == "MedicalRobot":
                #creates instance of robot
                mybot = MedicalRobot(row[1], row[2], row[3], battery, row[5])
                #appends that instance to robots 
                robots.append(mybot)
                
            if row[0] == "DriverRobot":
                mybot = DriverRobot(row[1], row[2], row[3], battery, row[5], row[6])
                robots.append(mybot)
            
            
        print(f'Processed {line_counter} lines.')
    return robots

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type = str, help = 'The name of the file withthe robots data')
    args = parser.parse_args(args_list)
    return args
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    robots = main(args.filename)
    for robot in robots:
        print(robot.talk())