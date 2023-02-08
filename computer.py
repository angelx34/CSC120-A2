class Computer:

    """
    creates atribute variables
    """
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int 

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    """
    constructor containing the computers information
    """
    def __init__(self, description, processor_type,hard_drive_capacity,memory,operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    """
    prints the details of the computer
    """
    def printDetails (self) :
        print (self.description)
        print (self.processor_type) 
        print (self.hard_drive_capacity) 
        print (self.memory)
        print (self.operating_system)
        print (self.year_made)
        print (self.price)

    """
    updates price and operating system
    """
    def update_price(self, new_price) : 
        self.price= new_price 
    def update_operating_system(self, New_OS) : 
        self.operating_system= New_OS
    # What methods will you need?