import smtplib
import time
co=0
while True:
    if co==10:
        break
    server=smtplib.SMTP("smtp.gmail.com",587)

    message="Subject: Buy Stonks\n\nBuy XXX Stonk"


    server.starttls()

    server.login("anindhith.genai@gmail.com","xatydrhgemkcesfs")

    server.sendmail("anindhith.genai@gmail.com","anindhith091204@gmail.com",message)

    print("Mail Sent")
    co+=1
    time.sleep(60)
    
