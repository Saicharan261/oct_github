from datetime import datetime

name=input("Enter your name:")
#list of items
list='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/kg
Panner  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 85/kg
'''
#Declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[] 

#rates per items
items={'rice':20,
       'sugar':30,
       'salt':20,
       'oil':80,
       'panner':110,
       'maggi':50,
       'boost':90,
       'colgate':85}
option=int(input("for list of items press 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")

    else:
        print("you entered worng number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","siddha supermarket",25*"=")
            print(28*" ","Medak25")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-",'TotalAmount:','Rs',totalprice)
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")