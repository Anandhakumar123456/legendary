#Date: 28-07-2023
#Day : Friday

#Inventary class:

class Inventory:
    def __init__(self,lst):
        self.inventories=lst
        

    def add(self,product_id,brand,buy_price,sell_price,qty):
        new_item={
            "Product ID":product_id,
            "Brand":brand,
            "Buy Price":buy_price,
            "Sell Price":sell_price,
            "Qty":qty
        }
        self.inventories.append(new_item)

    def remove(self,product_id):  
        for item in self.inventories:   #This line for find the product_id in the list.
            if item["Product ID"] ==product_id:  
                self.inventories.remove(item)
                break
        

    def print_all_details(self):
        for i in self.inventories:
            print(i)
        
        
    def details(self,product_id):
            for item in self.inventories:   
                if item["Product ID"]==product_id:
                    return item

inventories=[]


#Creating an Object for Inventory:

o=Inventory(inventories)


#Adding the details in the list:

o.add("001","Horlics",8,10,100)
o.add("002","Boost",3,5,58)
o.add("003","Born Vita",47,50,87)
o.add("004","Dairy Milk",17,20,92)


#Remove a particular item in the list based on Product ID:

print(o.remove("002"))


#print a particular item in the list based on Product ID:

print(o.details("003"))

#print All details in the list:

o.print_all_details()















