


# instance method, class method, static method 

class Student:


    school = 'Test'  # class variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1    # instance variable
        self.m2 = m2    # instance variable
        self.m3 = m3    # instance variable


    def avg(self):   # instance method
        return (self.m1+self.m2+self.m3)/3
    

    def get_m1(self):    # accessor method/getter -> fetch instance variable
        return self.m1
    
    def set_m1(self, value):   # mutator method/setter -> update/modify instance variable value
        self.m1 = value

    @classmethod
    def info(cls):      # class method
        return cls.school
    

    @staticmethod
    def get_something_new():   # static method
        print("Here I can do anything inside the class with static method")

    


s1= Student(10,20,30)
s2= Student(12,14,20)

print(s1.avg())
print(Student.info())
Student.get_something_new()
