import requests
import time

def get_price(url):
    response = requests.get(url)
    fullscript = response.text
    check=0
    allprices=""
    finalprice=""
    #All Prices
    for i in fullscript:
        if i=="₹":
            check=1
        if check==1:
            allprices+=i
            if i=="." or i=="<" or i=="|":
                check=0
    co=0
    avgprice=""
    lowprice=""
    #Current Price
    for i in allprices:
        if i=="₹":
            co+=1
        if co==5:
            finalprice+=i
        if co==2:
            avgprice+=i
        if co==1:
            lowprice+=i
            
    finalprice=finalprice[:-1]
    avgprice=avgprice[:-1]
    lowprice=lowprice[:-1]
    return finalprice,avgprice,lowprice

items={"Portronics Toad One Bluetooth Mouse":"https://pricehistory.app/p/portronics-toad-one-bluetooth-mouse-2-4-z31rxm2h",
"ZEBRONICS Shark Lite Wireless Gaming Mouse":"https://pricehistory.app/p/zebronics-shark-lite-wireless-gaming-mouse-4600dpi-HYo5vjmb",
"Ikigai":"https://pricehistory.app/p/ikigai-japanese-secret-long-happy-life-kKzP9vyp"
}


price=[]

co=0
while True:
    
    for pro_name in items:
        fin_pr,avg_pr,low=get_price(items[pro_name])
        print(pro_name,":",fin_pr)
        print("Average Price:",avg_pr)
        
        
        fin_pr=int(fin_pr[1:])
        avg_pr=int(avg_pr[1:])
        low=int(low[1:])
        
        if fin_pr<=low:
            print("Buy",pro_name)
        print()
    
    co+=1
    if co==2:
        break
    time.sleep(100)
    
