for i in range(5):
    print(i)

class rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def change_x(self, new_x):
        self.lenght = new_x

    def area(self):
        return self.length * self.width
