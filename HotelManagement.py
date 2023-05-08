class menucard:
    print("********************STREET FOODS**********************\n $$$$$$$$$$$$$$$$$$$$ Management$$$$$$$$$$$")
    def __init__(self,s=0,r=0,p=0,q=0,y=0):
        self.s=s
        self.r=r
        self.p=p
        self.q=q
        self.y=y
        
    def breakfast(self):
        print("1.idly........rs.22")
        print("2.vadai.......rs.35")
        print("3.pongal/upma......rs.55")
        print("4.poori/potato.....rs.68")
        print("5.dosai...........rs.61")
        print("6.masala dosai.....rs.73")
        print("7.podi dosai.......rs.69")
        print("8.podi masala dosai...rs.84")
        print("9.paper roast.......rs.87")
        print("10.paper roast masala....rs.97")
        print("11.ghee roast.........rs.91")
        print("12.ghee roast masala......rs.103")
        a=int(input("enter the items:"))
        if(a==1):
            b=int(input("enter the quantities:"))
            self.s=self.s+22*b
            print("breakfast rs.",self.s)
        elif(a==2):
            b=int(input("enter the quantities:"))
            self.s=self.s+35*b
            print("breakfast rs.",self.s)
        elif(a==3):
            b=int(input("enter the quantities:"))
            self.s=self.s+55*b
            print("breakfast rs.",self.s)
        elif(a==4):
            b=int(input("enter the quantities:"))
            self.s=self.s+68*b
            print("breakfast rs.",self.s)
        elif(a==5):
            b=int(input("enter the quantities:"))
            self.s=self.s+61*b
            print("breakfast rs.",self.s)
        elif(a==6):
            b=int(input("enter the quantities:"))
            self.s=self.s+73*b
            print("breakfast rs.",self.s)
        elif(a==7):
            b=int(input("enter the quantities:"))
            self.s=self.s+69*b
            print("breakfast rs.",self.s)
        elif(a==8):
            b=int(input("enter the quantities:"))
            self.s=self.s+84*b
            print("breakfast rs.",self.s)
        elif(a==9):
            b=int(input("enter the quantities:"))
            self.s=self.s+87*b
            print("breakfast rs.",self.s)
        elif(a==10):
            b=int(input("enter the quantities:"))
            self.s=self.s+97*b
            print("breakfast rs.",self.s)
        elif(a==11):
            b=int(input("enter the quantities:"))
            self.s=self.s+91*b
            print("breakfast rs.",self.s)
        elif(a==12):
            b=int(input("enter the quantities:"))
            self.s=self.s+103*b
            print("breakfast rs.",self.s)
        elif(a==13):
            exit()
        else:
            print("not available")
    def eveningtiffin(self):
         print("1.bonda...rs.63,\n2.bajji...rs.78,\n3.cutlet....rs.45,\n4.vadai...rs.65,\n5.mini idly...rs.76,\n6.plain dosa...rs.67,\n7.egg dosa.....rs.98,\n8.fried rice....rs.120,\n9.noodles....rs.90,\n10.tandoori...rs.150")
         d=int(input("enter the items:"))
         if(d==1):
             e=int(input("enter the quantities:"))
             self.r=self.r+63*e
             print("eveningtiffen rs.",self.r)
         elif(d==2):
             e=int(input("enter the quantities:"))
             self.r=self.r+78*e
             print("eveningtiffen rs.",self.r)
         elif(d==3):
             e=int(input("enter the quantities:"))
             self.r=self.r+45*e
             print("eveningtiffen rs.",self.r)
         elif(d==4):
             e=int(input("enter the quantities:"))
             self.r=self.r+65*e
             print("eveningtiffen rs.",self.r)
         elif(d==5):
             e=int(input("enter the quantities:"))
             self.r=self.r+76*e
         elif(d==6):
             e=int(input("enter the quantities:"))
             self.r=self.r+67*e
         elif(d==7):
             e=int(input("enter the quantities:"))
             self.r=self.r+98*e
             print("eveningtiffen rs.",self.r)
         elif(d==8):
             e=int(input("enter the quantities:"))
             self.r=self.r+120*e
             print("eveningtiffen rs.",self.r)
         elif(d==9):
             e=int(input("enter the quantities:"))
             self.r=self.r+90*e
             print("eveningtiffen rs.",self.r)
         elif(d==10):
             e=int(input("enter the quantities:"))
             self.r=self.r+150*e
             print("eveningtiffen rs.",self.r)
         elif(d==11):
             exit()
         else:
             print("not available")
    def sweet(self):
        print("1.gulab jamun....rs.60,\n2.rasagulla....rs.80,\n3.halwa....rs.65,\n4.rasamalai.....rs.90,\n5.paalgova.....rs.100")
        g=int(input("which sweet do you want:"))
        if(g==1):
            h=int(input("enter the quantities:"))
            self.p=self.p+60*h
            print("sweet rs.",self.p)
        elif(g==2):
            h=int(input("enter the quantities:"))
            self.p=self.p+80*h
            print("sweet rs.",self.p)
        elif(g==3):
            h=int(input("enter the quantities:"))
            self.p=self.p+65*h
            print("sweet rs.",self.p)
        elif(g==4):
            h=int(input("enter the quantities:"))
            self.p=self.p+90*h
            print("sweet rs.",self.p)
        elif(g==5):
            h=int(input("enter the quantities:"))
            self.p=self.p+100*h
            print("sweet rs.",self.p)
        elif(g==6):
            exit()
        else:
            print("not available")
    def junkfood(self):
        print("1.pizza.......rs.80,\n2.sandwich......rs.50,\n3.burger....rs.100,\n4.frenchfries....rs.60,\n5.chickenroll.....rs.67")
        i=int(input("enter the item u want:"))
        if(i==1):
            j=int(input("enter the quantities:"))
            self.q=self.q+80*j
            print("junkfood rs.",self.q)
        elif(i==2):
            j=int(input("enter the quantities:"))
            self.q=self.q+50*j
            print("junkfood rs.",self.q)
        elif(i==3):
            j=int(input("enter the quantities:"))
            self.q=self.q+100*j
            print("junkfood rs.",self.q)
        elif(i==4):
            j=int(input("enter the quantities:"))
            self.q=self.q+60*j
            print("junkfood rs.",self.q)
        elif(i==5):
            j=int(input("enter the quantities:"))
            self.q=self.q+67*j
            print("junkfood rs.",self.q)
        elif(i==6):
            exit()
        else:
            print("not available")
    def beverages(self):
        print("1.coffee....rs.20,\n2.tea....rs.35,\n3.horlicks....rs.45,\n4.boost....rs.50,\n5.milk....rs.45")
        n=int(input("enter the item:"))
        if(n==1):
            w=int(input("enter the quantities:"))
            self.y=self.y+20*w
            print("beverages rs.",self.y)
        elif(n==2):
            w=int(input("enter the quantities:"))
            self.y=self.y+35*w
            print("beverages rs.",self.y)
        elif(n==3):
            w=int(input("enter the quantities:"))
            self.y=self.y+45*w
            print("beverages rs.",self.y)
        elif(n==4):
            w=int(input("enter the quantities:"))
            self.y=self.y+50*w
            print("beverages rs.",self.y)
        elif(n==5):
            w=int(input("enter the quantities:"))
            self.y=self.y+45*w
            print("beverages rs.",self.y)
        elif(n==6):
            exit()
        else:
            print("not available")
    def display():
        print("breakfast",self.s)
        print("eveningtiffen",self.r)
        print("sweet",self.p)
        print("junkfood",self.q)
        print("beverages",self.y)
        
z=menucard()
while(1):
    print("1.breakfast,\n2.eveningtiffen,\n3.sweet,\n4.junkfood,\n5.beverages")
    u=int(input("enter the items:"))
    if(u==1):
        z.breakfast()
    if(u==2):
        z.eveningtiffin()
    if(u==3):
        z.sweet()
    if(u==4):
        z.junkfood()
    if(u==5):
        z.beverages()
            
            
        
        

        
            
            



    
