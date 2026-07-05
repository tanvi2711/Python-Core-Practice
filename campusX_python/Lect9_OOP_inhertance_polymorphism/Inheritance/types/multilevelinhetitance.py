class grandParent:

    def __init__(self,num):
        self.num=num


class parent(grandParent):

    def __init__(self, num,val):
        super().__init__(num)

        self.val=val


class child(parent):

    def __init__(self, num, val,var):
        super().__init__(num, val)

        self.var=var

    def show(self):
        print("GrandParent : ",self.num)
        print("Parent : ",self.val)
        print("Child : ",self.var)

son=child(100,50000,"Tanvi")
son.show()