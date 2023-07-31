#Date: 28-07-2023
#Day : Friday


#Inheritance:


class Person:
    def __init__(self,name,age,mobile): #constructor /Initilizer
        self.name=name   
        self.age=age     
        self.mobile=mobile 
        
    def details(self):  #Instance Method     #The function which is used in the class is called method.
        return {
            "Name" :self.name,
            "Age"  :self.age,
            "Mobile":self.mobile
        }
    

#Inheritance:

class Student(Person):
    def __init__(self, name, age, mobile,standard):
        super().__init__(name, age, mobile)
        self.standard=standard

    def details(self):
        std_info=super().details()
        std_info["standard"] =self.standard
        return std_info        



class Staff(Person):
    def __init__(self, name, age, mobile,salary):
        super().__init__(name, age, mobile)
        self.salary=salary

    def details(self):
        staff_info=super().details()
        staff_info["salary"] =self.salary
        return staff_info        

std1=Student("Anand",20,9876543210,12)
print(std1.details())


staff1=Staff("Ravi",29,8765432190,90000)
print(staff1.details())