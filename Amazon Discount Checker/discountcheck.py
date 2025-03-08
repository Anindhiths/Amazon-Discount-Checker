import tkinter as tk
from bs4 import BeautifulSoup
import requests
import time

def get_price(url):
    response = requests.get(url)
    fullscript = response.text
    check = 0
    allprices = ""
    finalprice = ""
    # All Prices
    for i in fullscript:
        if i == "₹":
            check = 1
        if check == 1:
            allprices += i
            if i == "." or i == "<" or i == "|":
                check = 0
    co = 0
    avgprice = ""
    lowprice = ""
    # Current Price
    for i in allprices:
        if i == "₹":
            co += 1
        if co == 5:
            finalprice += i
        if co == 2:
            avgprice += i
        if co == 1:
            lowprice += i

    finalprice = finalprice[:-1]
    avgprice = avgprice[:-1]
    lowprice = lowprice[:-1]
    return finalprice, avgprice, lowprice

update = 0
def update_prices():
    global update
    display_text = f"No of Refreshes: {update}\n"
    update += 1
    for pro_name in items:
        fin_pr, avg_pr, low = get_price(items[pro_name])
        display_text += f"{pro_name}:\nCurrent Price: {fin_pr}\nAverage Price: {avg_pr}\n"
        
        fin_pr_value = int(fin_pr[1:])
        avg_pr_value = int(avg_pr[1:])
        low_value = int(low[1:])

        if fin_pr_value <= low_value:
            recommendation_label = tk.Label(root, text=f"Buy {pro_name}!", fg="green", font=("Arial", 32))
        else:
            recommendation_label = tk.Label(root, text="Wait for a lower price.", fg="red", font=("Arial", 32))

        recommendation_label.pack(pady=5, anchor="w")
    
    result_label.config(text=display_text)
    no_of_sec = 100  # Refresh every ... seconds
    root.after(no_of_sec * 1000, update_prices)

# Product URLs
items = {
    "Portronics Toad One Bluetooth Mouse": "https://pricehistory.app/p/portronics-toad-one-bluetooth-mouse-2-4-z31rxm2h",
    "ZEBRONICS Shark Lite Wireless Gaming Mouse": "https://pricehistory.app/p/zebronics-shark-lite-wireless-gaming-mouse-4600dpi-HYo5vjmb",
    "Ikigai": "https://pricehistory.app/p/ikigai-japanese-secret-long-happy-life-kKzP9vyp"
}

# Create GUI
root = tk.Tk()
root.title("Price Tracker")
root.geometry("600x600")

# Create title label (bold and underlined)
title_label = tk.Label(root, text="Product Price Tracker", font=("Arial", 40, "bold", "underline"))
title_label.pack(pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Arial", 32), anchor="w")
result_label.pack(pady=10)

# Start updating prices
update_prices()

# Run the tkinter loop
root.mainloop()
