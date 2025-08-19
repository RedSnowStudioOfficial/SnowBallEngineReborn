class A:
    def __init__(self):
        self.x = 0
    
    def set_x(self, x):
        self.x = x

class B(A):
    def __init__(self):
        super().__init__()
    
    def pause(self):
        print(self.x)

    def get_x(self):
        return self.x

    def get_x_from_class(self, object):
        return object.get_x()


a = B()
b = B()

b.set_x(12)

a.set_x(22)
a.pause()

print(a.get_x_from_class(b))