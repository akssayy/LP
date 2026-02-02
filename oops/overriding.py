class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

        
b = B()
b.show()