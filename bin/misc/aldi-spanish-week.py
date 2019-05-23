#!/usr/bin/env python

import bs4, requests, smtplib

getPage = requests.get('https://www.lidl.co.uk/en/Offers.htm?week=1')
getPage.raise_for_status() #if error it will stop the program

content = bs4.BeautifulSoup(getPage.text, 'html.parser')
images = content.findAll('img')
spain = 'slot_image_spain.png'
available = False

for image in images:
    if image['alt'] == 'Flavour of the Week':
        if image['src'].find(spain) != -1:
            available = True

if available == True:
    print('Spanish week in Aldi :-)')
else:
    print('No Spanish week :-(')
