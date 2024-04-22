#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[25]:


# Connect to the website

URL = "https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=nav_signin?customId=B0752XJYNL&dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&th=1&customizationToken=MC_Assembly_1%23B0752XJYNL"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-66260f93-1271ee9758bf5c7c67d6455e"}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id = "priceblock_ourprice").get_text()

print(soup2)



# In[26]:


price = price.strip()[1:]
title = title.strip()


# In[29]:


import datetime

today = datetime.date.today()

print(today)


# In[ ]:


import csv

header = ["Title","Price","Date"]
data = [title, price, today]

with open('AmazonWebScraperDataset.csv','w',newline = '',encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[30]:


import pandas as pd

df = pd.read_csv('C:\Users\kamier\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


#We are appending data to CSV
with open('AmazonWebScraperDataset.csv','w',newline = '',encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


def check_price():
    URL = "https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=nav_signin?customId=B0752XJYNL&dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&th=1&customizationToken=MC_Assembly_1%23B0752XJYNL"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-66260f93-1271ee9758bf5c7c67d6455e"}

    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id = "priceblock_ourprice").get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ["Title","Price","Date"]
    data = [title, price, today]
    
    with open('AmazonWebScraperDataset.csv','w',newline = '',encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\kamier\AmazonWebScrapingDataset.csv')

print(df)


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('kamiering.kuerbanjiang@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Kam, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'kamiering.kuerbanjiang@gmail.com',
        msg
     
    )


# In[ ]:





# In[ ]:





# In[ ]:




