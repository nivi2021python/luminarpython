class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

c=Calc(8,4)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())