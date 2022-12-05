""" A driving range for test-driving instances of the Car class. """
from math import cos, dist, radians, sin, pi


def main():
    """ Create the application. """

class Car():
    '''
    Class to represent a Car
    
    Attributes 
    ---------
    x: float 
        starting x coordiate of the car 
    y: float
        starting y coordinate of the car 
    heading: float 
        the starting heading
    
    '''
    def __init__(self, x=0, y=0, heading =0):
        '''
        Constructs all the necessary attributes for the car object 
        
        
        parameters  
        ---------
            x: float 
                starting x coordiate of the car 
            y: float
                starting y coordinate of the car 
            heading: float 
                the starting heading
        
        '''
        self.x = x
        self.y = y
        self.heading = heading

    def turn(self, NumOfDegrees):
        '''
        Method to turn the car given a number of degrees
        
        
        parameters:
        ----------
            NumOfDegrees: float 
                Number of degrees to turn 
                
        returns:
            self.heading: float
                - value takes the specified numofdegrees and adds it to heading and reduces it my % 360
        
        '''
        #postitive number of degrees represents a clockwise turn
        #negative represents a counter clockwise turn 
        self.NumOfDegrees =NumOfDegrees


        #adds specified degrees to heading and reduces it by %360, returns value to heading 
        self.heading = (self.heading + NumOfDegrees) % 360
        #return heading value to turn method 
        return self.heading 

    def drive(self, distance):
        '''
        method to drive the car 
        
        parameters: 
        ---------
            distance: float 
                - distance the car will travel
                
            d: Float
                - assigns distance to d 
            h: float
                -assigns heading to h 
                
        side effects: 
        --------

            heading now defined as h 
            Changes headings value to convert to radians 
            
        
        '''
        self.distance = distance 
        #assign d to distance
        d = self.distance    
        #degrees converted to radians is h 
        h = self.heading * pi/180


        #formula for x coords
        self.x += d * sin(h)
        #formula for y coords
        self.y -= d * cos(h)



def sanity_check():
    '''
    creates an instance of the car class that takes turn and drive 
    prints the location and heading of the car  
    
    returns:
        Mycar: the instance of the Car Class 
    
    '''
    
    #creates an instance of the car class and pass through arguments for it to move a certain amount 
    myCar = Car()
    myCar.turn(90)
    myCar.drive(10)
    myCar.turn(30)
    myCar.drive(20)
    #prints the coords of the car class 
    print(myCar.x, myCar.y)
    #prints the heading of the car class 
    print(myCar.heading)
    #returns instance of mycar 
    return myCar
    




if __name__ == "__main__":
    sanity_check()
