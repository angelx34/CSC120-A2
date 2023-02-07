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
    

   # def printInventory(self):
        #for c in self inventory

def main():            
    myStore= ResaleShop()
    myStore.buy("A","A", "A","A" ,"A","A","A")        
    print(myStore.inventory)# for big one specify all the description 
main()
          
            


 # You'll remove this when you fill out your constructor

    # What methods will you need?
   
