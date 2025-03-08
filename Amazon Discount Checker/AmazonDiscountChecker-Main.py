import tkinter as tk
from bs4 import BeautifulSoup
import requests
import time

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
"""
def send_email(product_name, current_price):
    
    subject = f"Price Alert: Buy {product_name} Now!"
    body = f"The price of {product_name} has dropped to {current_price}. It's time to buy!"

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to the email
    message.attach(MIMEText(body, "plain"))
    text = message.as_string()

    # Send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print(f"Email sent to {receiver_email} about {product_name}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

"""

def get_price(url):
    response=requests.get(url)
    fullscript=response.text
    check=0
    allprices=""
    finalprice=""
    # All Prices
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
    
    # Current Price
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

update=0
def update_prices():
    global update
    display_text="No of Refreshes: "+str(update)+"\n"
    update+=1
    for pro_name in items:
        fin_pr,avg_pr,low=get_price(items[pro_name])
        display_text += f"{pro_name}:\nCurrent Price: {fin_pr}\nAverage Price: {avg_pr}\nLowest Price: {low}\n"
        
        fin_pr_value=int(fin_pr[1:])
        avg_pr_value=int(avg_pr[1:])
        low_value=int(low[1:])

        if fin_pr_value<=low_value:
            #send_email(pro_name, fin_pr)
            display_text+=f"Buy {pro_name}!\n"
        else:
            display_text+="Wait for a lower price.\n"

        display_text+="\n"
    
    result_label.config(text=display_text)
    no_of_sec=60 # Refresh every x seconds
    root.after(no_of_sec*1000,update_prices)  

# Product URLs
items = {
    "Logitech G502 Wireless Gaming Mouse Black":
    "https://pricehistory.app/p/logitech-g502-lightspeed-wireless-gaming-mouse-hero-9ILn27G5",
    "Razer Basilisk Wireless Gaming Mouse Matte Black":
    "https://pricehistory.app/p/razer-basilisk-v3-x-hyperspeed-wireless-gaming-zruSWsSj",
    "Ikigai Book":
    "https://pricehistory.app/p/ikigai-japanese-secret-long-happy-life-kKzP9vyp",
    "Sandisk 4TB SSD Black Color":
    "https://pricehistory.app/p/sandisk-extreme-portable-4tb-1050mb-s-r-2NEuA3Q2"
    
}


root = tk.Tk()
root.title("Price Tracker")
root.geometry("4020x1080")


title_label = tk.Label(root, text="Product Price Tracker", font=("Arial", 40,"bold", "underline"))
title_label.pack(pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Arial", 25), anchor="w")
result_label.pack(pady=10)

update_prices()

root.mainloop()
