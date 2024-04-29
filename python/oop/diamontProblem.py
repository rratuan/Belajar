class A:
    def show(self):
        print("Show A")

class B(A):
    def show(self):
        print("Show B")

class C(A):
    def show(self):
        print("Show C")

class D(B,C):
    pass

objek = D()
# help(objek) uncomment untuk melihat urutan (method resolution order)
objek.show()