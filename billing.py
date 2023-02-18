import time
class Billing:
    amt_veg_pizza=120
    n_veg_pizza=0
    extra_toppings=0
    amt_corn_cheese=300
    n_corn_cheese=0
    extra_cheese=0
    amt_barbque=250
    n_barbque=0
    extra_chicken=0
    n_paneer=0
    amt_panner=200
    gst=20
    serviceTax=30
    def __init__(self,total):                    #passing a constructor to get access in any method in this class
        self.total=total
        
    def veg_pizza(self):
        Billing.n_veg_pizza+=1
        print("------------------------------------")
        opt2=input("DO YOU NEED ANY EXTRA TOPPINGS <Y/N>:-")
        print("------------------------------------")
        if opt2=="y" or opt2=="Y":
            Billing.extra_toppings+=40
            print("\namt=",Billing.amt_veg_pizza,"\nGST=",Billing.amt_veg_pizza*(Billing.gst/100),"\nservice tax=",Billing.serviceTax,"\nextra topping=","40")
        else:   
            print("\namt=",Billing.amt_veg_pizza,"\nGST=",Billing.amt_veg_pizza*(Billing.gst/100),"\nservice tax=",Billing.serviceTax)  #prints the amount of that particular order
        self.total+=Billing.amt_veg_pizza+Billing.amt_veg_pizza*(Billing.gst/100)+Billing.serviceTax+Billing.extra_toppings   #keep updates the total amount
        print("------------------------------------")

        
    def corn_cheese_pizza(self):
        Billing.n_corn_cheese+=1
        #amt=300
        #extraCheese=50
        print("------------------------------------")
        cheese=input("did you want extra cheese press <Y/N>:-")   #asks for extra cheese
        print("------------------------------------")
        if cheese=="y" or cheese=="Y":
            Billing.extra_cheese+=50
            print("------------------------------------")
            print("\namt=",Billing.amt_corn_cheese,"\nGST=",Billing.amt_corn_cheese*(Billing.gst/100),"\nservice tax=",Billing.serviceTax,"\nextra cheese=",Billing.extra_cheese)
            print("------------------------------------")
        else:                                                   #if they don't want extra cheese
            print("------------------------------------")
            print("\namt=",Billing.amt_corn_cheese,"\nGST=",Billing.amt_corn_cheese*(Billing.gst/100),"\nservice tax=",Billing.serviceTax) 
            print("------------------------------------")
        self.total+=Billing.amt_corn_cheese+Billing.amt_corn_cheese*(Billing.gst/100)+Billing.serviceTax+Billing.extra_cheese
        print("------------------------------------")

                    
    def barbque_chicken_pizza(self):
        Billing.n_barbque+=1
        #amt=250
        #extra_chicken=100
        print("------------------------------------")
        opt2=input("do you want extra chicken press <Y/N>:-")
        print("------------------------------------")
        if opt2=="y" or opt2=="Y":
            Billing.extra_chicken+=50
            print("------------------------------------")
            print("\namt=",Billing.amt_barbque,"\nGST=",Billing.amt_barbque*(Billing.gst/100),"\nservice tax=",Billing.serviceTax,"\nextra chicken=",Billing.extra_chicken)
            print("------------------------------------")
        else:
            print("------------------------------------")
            print("\namt=",Billing.amt_barbque,"\nGST=",Billing.amt_barbque*(Billing.gst/100),"\nservice tax=",Billing.serviceTax)
            print("------------------------------------")
        self.total+=Billing.amt_barbque+Billing.extra_chicken+Billing.amt_barbque*(Billing.gst/100)+Billing.serviceTax
        

        print("------------------------------------")

        
    def paneer_tikka_pizza(self):
        Billing.n_paneer+=1
        #amt=200
        print("------------------------------------")
        print("\namt=",Billing.amt_panner,"\nGST=",Billing.amt_panner*(Billing.gst/100),"\nservice tax=",Billing.serviceTax)
        self.total+=Billing.amt_panner+Billing.amt_panner*(Billing.gst/100)+Billing.serviceTax
        print("------------------------------------")

        
    def menu(self):
        print("------------------------------------")       #prints menu
        opt=input("PLEASE GIVE YOUR ORDER\n1.veg pizza-120\n2.corn cheese pizza-300\n3.Barbque chiicken pizza-250\n4.paneer tikka pizza-200\n\n")
        print("------------------------------------")
        if opt=="1":                                        #if elif's conditions will help us to generate bill as per their requirement
            time.sleep(1)
            pizza.veg_pizza()
        elif opt=="2":
            time.sleep(1)
            pizza.corn_cheese_pizza()
        elif opt=="3":
            time.sleep(1)
            pizza.barbque_chicken_pizza()
        elif opt=="4":
            time.sleep(1)
            pizza.paneer_tikka_pizza()
        else:
            print("ENTER CORRECT OPTION PLEASE\n")
    def final(self):
        print("------------------------------------")
        if Billing.n_veg_pizza > 0:
            print("no of veg pizzas=",Billing.n_veg_pizza,"*",(Billing.amt_veg_pizza+Billing.extra_toppings))
        if Billing.n_corn_cheese > 0:
            print("\nno of corn cheese pizzas=",Billing.n_corn_cheese,"*",(Billing.amt_corn_cheese+Billing.extra_cheese))
        if Billing.n_barbque>0:
            print("\nno of barbque pizzas=",Billing.n_barbque,"*",(Billing.amt_barbque+Billing.extra_chicken))
        if Billing.n_paneer>0:
            print("\nno of paneer tikka pizzas=",Billing.n_paneer,"*",Billing.amt_panner)
        print("YOUR ORDER WILL BE SHORTLY DELIVERED")
        print("TOTAL BILL= ",self.total)   #printing final bill
        print("------------------------------------")
        

print("------------------------------------")
print("\t\tWELCOME TO THE PIZZA HUT")
pizza=Billing(0)#creating an object and passing total amount
pizza.menu()
while True:                                   #To continue the order 
    print("------------------------------------")                     
    opt2=input("do you want to continue the order <Y/N>:-")
    if opt2=="y" or opt2=="Y":
        pizza.menu()
    else:
        break
pizza.final() #To print final bill
    
    






