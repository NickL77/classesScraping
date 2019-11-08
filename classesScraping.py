from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from twilio.rest import Client
from twilioAcctInfo import *

#Allow firefox to run headless (no GUI) 
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
-
#Get html source
url = "https://classes.berkeley.edu/content/2019-spring-anthro-2ac-001-lec-001"
browser.get(url)
html_source = browser.page_source
-
#Parse HTML to get number of interest
soup = BeautifulSoup(html_source, 'lxml')
num_seats_left = int(soup.find("span", {"class": "fspmedium"}).text)
browser.quit()

#Twilio account info
client = Client(account_sid, auth_token)

if num_seats_left == 16:
       msg = 'Same Same :/'
       for person in destination_num:
               message = client.messages.create(body=msg, from_=my_num, to=person)
else:
       msg = 'No longer 16 seats left!'
       for person in destination_num:
               message = client.messages.create(body=msg, from_= my_num, to=person)

