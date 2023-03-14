from bs4 import BeautifulSoup
from lxml import etree


with open('./src/xato_uzbek-russian.html') as f:
    soup = BeautifulSoup(f, "lxml")


translate_block = soup.select('div.ru div, i')


for cell in translate_block:
    if len(cell) > 0:
        print(cell, '\n')
