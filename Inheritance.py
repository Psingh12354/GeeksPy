class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B(A): #inheritinh A by B(A)
    def feature3(self):
        print("Feature 1 working")
    def feature4(self):
        print("Feature 2 working")
class C(A,B):
    def feature5(self):
        print("Multilevel")
a1=A()
a1.feature1()
a1.feature1()
b1=B()
