class parent:

    def __init__(self):
        self.num=100

    
class child(parent):

    def __init__(self, num):
        super().__init__()
        self.var=200

    def show(self):
        print(self.num)
        print(self.var)


# self hi son hai

son=child()
print(son.show())