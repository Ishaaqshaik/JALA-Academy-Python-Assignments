class A:  
    def display(self):
        print("Display Inside class A")
    
    def show(self):
        print("Show Inside class A")
    
class B(A):  
    def print_msg(self):
        print("Print Inside class B")
    
    def show(self):
        print("Show Inside class B")
    


class C(B): 
    def show(self):
        print("Show Inside class C")

print("=== Calling A class methods ===")
a = A()
a.display()
a.show()

print("\n=== Calling B class methods ===")
b = B()
b.display()    
b.print_msg()
b.show()       

print("\n=== Calling C class methods ===")
c = C()
c.display()   
c.print_msg()  
c.show()       

