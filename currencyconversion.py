class currency:
    def intro(self):
        print ("Select conversion")

    def inrtodollar(self):
        x=float(input("Enter currency to convert: "))
        conv = x/73.15
        #round(conv)
        print("Conversion is: ",round(conv,3),"dollar")
        
    def dollartoinr(self):
        x=float(input("Enter currency to convert: "))
        conv = x*73.15
        print("Conversion is: ",round(conv,3),"inr")

    def inrtopound(self):
        x=float(input("Enter currency to convert: "))
        conv=x/103.58
        print("Conversion is: ",round(conv,3),"pound")

    def poundtoinr(self):
        x=float(input("Enter currency to convert: "))
        conv=x*103.58
        print("Conversion is: ",round(conv,3),"inr")

    def inrtodirham(self):
        x=float(input("Enter currency to convert: "))
        conv=x/19.91
        print("Conversion is: ",round(conv,3),"dirham")

    def dirhamtoinr(self):
        x=float(input("Enter currency to convert: "))
        conv=x*19.91
        print("Conversion is: ",round(conv,3),"inr")

    def inrtoeuro(self):
        x=float(input("Enter currency to convert: "))
        conv=x/88.99
        print("Conversion is: ",round(conv,3),"euro")

    def eurotoinr(self):
        x=float(input("Enter currency to convert: "))
        conv=x*88.99
        print("Conversion is: ",round(conv,3),"inr")

c=currency()
c.intro()
while True:
    print('''
        1. Inr to Dollar
        2. Dollar to Inr
        3. Inr to Pound
        4. Pound to Inr
        5. Inr to Dirham
        6. Dirham to Inr
        7. Inr to Euro
        8. Euro to Inr
        9. Exit
     ''')
    print("                ")
    select=int(input("Enter your choice to make conversion: "))
    if select==1:
        c.inrtodollar()

    elif select==2:
        c.dollartoinr()

    elif select==3:
        c.inrtopound()

    elif select==4:
        c.poundtoinr()

    elif select==5:
        c.inrtodirham()

    elif select == 6:
        c.dirhamtoinr()

    elif select == 7:
        c.inrtoeuro()

    elif select == 8:
        c.eurotoinr()

    elif select==9:
        exit()
    else:
        print("Invalid Input")