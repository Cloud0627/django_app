class tashizan():

    def __init__(self):
        self.name = "name"
        self.age = 1

    def tasu(self,x,y):
        print(vars(self))
        print(self.name)
        self.age = 2 
        print(self.age)
        return x + y

