n=0
class Bank:

    bankname="SBI"
    def accCreate(self,acc_num,name):
        self.acc_num=acc_num
        self.name=name
        self.minimum_bal=5000
        self.bal=self.minimum_bal
    def deposit(self,amt):
        self.amt=amt
        self.bal+=self.amt
        print("your",Bank.bankname,"account has been credited with amount",self.amt)
        print("your current bsalance=",self.bal)
    def withdraw(self,amt):
        self.amt=amt
        if self.amt>self.bal:
            print("insufficient bal..!!!")
        else:
            print("account debited with",self.amt)
            self.bal-=self.amt
            print("available balance =", self.bal)
obj=Bank()
obj.accCreate(123,"abc")
obj.deposit(2500)
obj.withdraw(1000)