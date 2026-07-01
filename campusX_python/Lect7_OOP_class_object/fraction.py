class fraction:

    # paameterise constructor
    def __init__(self,x,y):
        self.num=x
        self.deno=y

    
    def __str__(self):
        return '{} / {}'.format(self.num,self.deno)


    def __add__(self,other):
        new_num=self.num*other.deno + other.num*self.deno
        new_deno=self.deno*other.deno


        return '{} / {}'.format(new_num,new_deno)
    
    def __sub__(self,other):
        new_num=self.num*other.deno - other.num*self.deno
        new_deno=self.deno*other.deno


        return '{} / {}'.format(new_num,new_deno)
    

    def __mul__(self,other):
        new_num=self.num*other.num
        new_deno=self.deno*other.deno


        return '{} / {}'.format(new_num,new_deno)
    
    def __truediv__(self,other):
        new_num=self.num*other.deno
        new_deno=self.deno*other.num


        return '{} / {}'.format(new_num,new_deno)


    def convert_to_deci(self):
        return self.num/self.num



num=int(input("Enter numerator: "))
deno=int(input("Enter denominator: "))

frac1=fraction(num,deno)
frac2=fraction(1,2)

print(frac1)
print("Decimal:",frac1.convert_to_deci())
print("ADDITION: " , frac1+frac2)
print("SUBSTRACTION:",frac1-frac2)
print("MULTIPLICATION:",frac1*frac2)
print("DIVISION:",frac1/frac2)