class Father:
    def show1(self):
        print("Father class")

class Mother:
    def show2(self):
        print("Mother class")

class Child(Father, Mother):
    def show3(self):
        print("Child class")

c = Child()
c.show1()
c.show2()
c.show3()