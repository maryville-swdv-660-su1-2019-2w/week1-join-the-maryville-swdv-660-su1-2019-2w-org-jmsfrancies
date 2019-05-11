import sys
import os

class IceCream:
    def __init__(self,ID,Flavor,Brand,Quantity,Cost):
        self.ID = ID
        self.Flavor = Flavor
        self.Brand = Brand
        self.Quantity = Quantity
        self.Cost = Cost
    def getOptions(self):
        return "\n{0}\n{1}\n{2}\n{3}\n{4}".format(self.ID,self.Flavor,self.Brand,self.Quantity,self.Cost)


IceCream_1 = IceCream(1,"Vanilla","Breyers",5,5.25)
IceCream_2 = IceCream(2,"Chocolate","Baskins-Robbins",6,2.25)
IceCream_3 = IceCream(3,"Cookie Dough","Blue Bell",2,7.00)
IceCream_4 = IceCream(4,"Cookies 'n' Cream","Cold Stone Creamery",10,5.50)
IceCream_5 = IceCream(5,"Smores","Dairy Queen",4,4.50)
IceCream_6 = IceCream(6,"Moose Tracks","Blue Bunny",1,11.00)

def main():
    i = input(" Would you like to preview Ice Cream Options: (yes/no): ")
    if i == "yes":
        print(IceCream_1.getOptions(),"\n",
           IceCream_2.getOptions(),"\n",
           IceCream_3.getOptions(),"\n",
           IceCream_4.getOptions(),"\n",
           IceCream_5.getOptions(),"\n",
           IceCream_6.getOptions(),"\n")
        x = input("Press Enter to Exit: ")
    else:
        print("An Apple a day keeps the Doctor Away!")
        x = input("Press Enter to Exit: ")

main()