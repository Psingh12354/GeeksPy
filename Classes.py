class Computer:
    #when have two variable
    def __init__(self,a,b):
        self.a=a;
        self.b=b;

        self.name="Priyanshu"
    def config(self):
        print("Sum : ",self.a+self.b)
        print("Hello World")
com1=Computer(5,5) #three variable passing 2 input and com1 object
Computer.config(com1)
print(com1.name)
