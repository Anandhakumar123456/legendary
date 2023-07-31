#Date: 31-07-2023
#Day : Monday


#Inheritance:



#Composition: 

class Salary:
    def __init__(self,m_salary) -> None:
        self.m_salary=m_salary

    def calculate_annual_salary(self,bonus=0):
        annual_salary=self.m_salary*12
        return annual_salary+bonus

#sal=Salary(10000)
#print(sal.calculate_annual_salary(5000)) #bonus    

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
        self.m_salary=salary
        self.salary=Salary(salary) #This is composition  is  createting object in another class .

    def details(self):
        staff_info=super().details()
        staff_info["salary"] =self.salary
        return staff_info        

    def get_salary_info(self,bonus=0):
        return self.salary.calculate_annual_salary(bonus)


stf1=Staff("Anand",20,6382812423,1000000)
print("Total salary is :"+str(stf1.get_salary_info(20000)))
