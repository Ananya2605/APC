class Grandfather:
    def show1(self):
        print("Grandfather class")

class Father(Grandfather):
    def show2(self):
        print("Father class")

class Son(Father):
    def show3(self):
        print("Son class")

s = Son()
s.show1()
s.show2()
s.show3()