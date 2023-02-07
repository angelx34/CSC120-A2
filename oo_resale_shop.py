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

    def refurbish(self,item_id,new_os): 
        for item_id in self.inventory : 
            if item_id == self.inventory.index(c) : # locate the computer
                if int(["year_made"]) < 2000:
                    item_id["price"] = 0 # too old to sell, donation only
                elif int(item_id["year_made"]) < 2012:
                    item_id["price"] = 250 # heavily-discounted price on machines 10+ years old
                elif int(item_id["year_made"]) < 2018:
                    item_id["price"] = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    item_id["price"] = 1000 # recent stuff
                if new_os is not None:
                    item_id["operating_system"] = new_os # update details after installing new OS
            else:
                print("Item", item_id, "not found. Please select another item to refurbish.")
    
    def printInventory(self,description, processor_type,hard_drive_capacity,memory,operating_system, year_made, price):
        for c in self.inventory: 
            c.print.Details(description, processor_type,hard_drive_capacity,memory,operating_system, year_made, price)

def main():            
    myStore= ResaleShop()
    myStore.buy("A","A", "A","A" ,"A","A","A")        
    print(myStore.inventory)# for big one specify all the description 
main()
          
            


 # You'll remove this when you fill out your constructor

    # What methods will you need?
   
