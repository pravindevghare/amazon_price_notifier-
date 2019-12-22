

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

# send a request to fetch HTML of the page
response = requests.get('https://www.amazon.in/dp/B07N9DNJ62?pf_rd_p=c2d9f93b-456a-4319-8315-b7aa154df8b7&pf_rd_r=M51WWQEGQ530DVZYY9VH', headers=headers)

# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')


# function to check if the price has dropped below 20,000
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  

  #converting the string amount to float
  converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 9000):
    send_mail()

  #using strip to remove extra spaces in the title
  print(title.strip())




# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('pravindevghare4@gmail.com', '******')

  subject = 'Price Fell Down'
  body = "Check the amazon link https://www.amazon.in/dp/B07N9DNJ62?pf_rd_p=c2d9f93b-456a-4319-8315-b7aa154df8b7&pf_rd_r=M51WWQEGQ530DVZYY9VH "

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'pravindevghare4@gmail.com',
    'xyz@gmail.com',
    msg
  )
  #print a message to check if the email has been sent
  print('Hey Email has been sent')
  # quit the server
  server.quit()

#loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60 * 60)
