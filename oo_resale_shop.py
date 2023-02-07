from computer import *

class ResaleShop:

    # What attributes will it need? 
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
       
    def __init__(self): 
        self.inventory= []

    def buy (self,description, processor_type,hard_drive_capacity,memory,operating_system, year_made, price) : 
        c= Computer(description, processor_type,hard_drive_capacity,memory,operating_system, year_made, price)
        self.inventory.append(c)

    def sell (self,description, processor_type,hard_drive_capacity,memory,operating_system, year_made, price):
        c= Computer(description, processor_type,hard_drive_capacity,memory,operating_system, year_made, price)
        self.inventory.remove(c) 

    def refurbish(self,c,new_os): 
        if c in self.inventory : 
            if c == self.inventory.index(c) : # locate the computer
                if c.year_made < 2000:
                    c.price = 0 # too old to sell, donation only
                elif c.year_made < 2012:
                    c.price = 250 # heavily-discounted price on machines 10+ years old
                elif c.year_made < 2018:
                    c.price = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    c.price = 1000 # recent stuff
                if new_os is not None:
                    c.price = new_os # update details after installing new OS
            else:   
                print("Item", c, "not found. Please select another item to refurbish.")
    
    def printInventory(self):
        for c in self.inventory: 
            c.print.Details() 

    def update_price(self,c, new_price) : 
        if c in self.inventory :
            self.computer.price= new_price

    def update_price(self,c, new_OS) : 
        if c in self.inventory :
            self.computer.operating_system= new_OS
def main():            
    
           
    print(myStore.inventory)# for big one specify all the description 
main()
          
            


 # You'll remove this when you fill out your constructor

    # What methods will you need?
   
