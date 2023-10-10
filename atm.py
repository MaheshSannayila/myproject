class atm():
    def __init__ (self ):
        self.acount_balence=0
    def genarate_atm_pin(self,atmpin):
        self.atmpin=atmpin
        return ("successfully genarated your  pin: ",atmpin)
    def bal_enquiry(self,user_pin):
        if self.atmpin==user_pin:

            return ("your acount balnce is :",self.acount_balence)
        else:
            return ("incorrect pin")
                  
    def deposite_in_acount(self,user_pin,amount):
        if self.atmpin==user_pin:
            self.amount=amount
            self.acount_balence+=amount
            return ("successfully deposited your acount bal is :",self.acount_balence)
        else:
            return ("incorrect pin")
        
    def withdraw_money(self,user_pin,amount):
        self.amount=amount
        if self.atmpin==user_pin:
            if self.acount_balence>amount:
                self.acount_balence-=amount
                return "successfully withdraw your acount bal is: ",self.acount_balence
            else:
                print( "insuffecient balence")
        else:
            print("incorrect pin")

atm_obj=atm()
atm_obj.genarate_atm_pin(1234)
atm_obj.deposite_in_acount(1234,5000)
atm_obj.deposite_in_acount(1234,10000)
atm_obj.withdraw_money(1234,16000)
print(atm_obj.bal_enquiry(1234))
