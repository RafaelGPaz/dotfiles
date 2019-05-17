#! python3
import bs4, requests, smtplib

toAddress = 'mr.rafaelgp@gmail.com'

#Download page
getPage = requests.get('https://www.lidl.co.uk/en/Offers.htm?week=1')
getPage.raise_for_status() #if error it will stop the program

content = bs4.BeautifulSoup(getPage.text, 'html.parser')
images = content.findAll('img')
spain = 'slot_image_spain.png' # This is the name of the food you are looking for
available = False

for image in images:
    if image['alt'] == 'Flavour of the Week':
        if image['alt'].find(spain) == -1:
            available = True

if available == True:
    print('Spanish week in the Aldi')
else:
    print('No Spanish week')
