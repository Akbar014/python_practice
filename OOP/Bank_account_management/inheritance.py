
class A:        # super class / Parent class

    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

    
class B(A):     # B is inheriting A . # sub class / child class
    def new_feature(self):
        print("This is new feature from class b")


# this is single level inheritance 

class c(B):
    def feature4(self):
        print("This is from feature4")

# this is multi level inheritance  (A<-b<-c)




class c(A,B):
    def feature4(self):
        print("This is from feature4")

# this is multiple inheritance (c<-A, c<-B)

obj = B()

obj.feature1()