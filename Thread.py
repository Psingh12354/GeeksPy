from time import *
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(50):
            print(" Hi")
t1=Hello()            
t2=Hi()
t1.run()
t2.run()
print("Run over")
t1.start()
t2.start()
t1.join()
t2.join()
print("bye")
