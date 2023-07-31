#Date: 27-07-2023
#Day : Thursday



#class creation:

#syntax - 
# class class_name():

class vehicle():
    def __init__(self,model,color,speed):
        self.model=model
        self.color=color
        self.speed=speed

    def details(self):
        return {
            "Brand" :self.model,
            "Color" :self.color,
            "Max_speed" :f"{self.speed} kmph"
        }    
    


#Audi car:

audi=vehicle("Audi","White",200)
print(audi.details())

#BMW car:

BMW=vehicle("BMW","Black",259)
print(BMW.details())

