import datetime

import requests
from bs4 import BeautifulSoup
import re
import sys

def main(*arguments):
    finaltext = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n"
    baseurl="https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod="
    #add= input("Fon Kodu Giriniz: ")

    if arguments is None:
        arguments= sys.argv[1:]

    arguments= list(arguments)

    for add in arguments:

        url= baseurl+add

        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser")
        all_text = ''.join(soup.stripped_strings)

        #first 1000 characters of the string
        all_text = all_text[500:800]
        name= re.findall(f'{"Analiz"}(.*?){"Son"}', all_text)[0]
        #print(name)




       # print(all_text)
        increment = re.findall(f'{re.escape(")%")}(.*?){"Pay"}', all_text)[0]
        price= re.findall(f'{re.escape("t (TL)")}(.*?){"Günlük"}', all_text)[0]




        increment = increment.replace(',','.')
        price = price.replace(',','.')
        #convert to float
        price = float(price)
        increment = float(increment)


        #merge argument, price and increment in a string.
        result = f'FON= {name}\nKOD= {add}\nPRICE= {price}\nCHANGE= {increment}\n\n'
        #print(result)
        finaltext += result
    #print(finaltext)
    return finaltext

if __name__ == '__main__':
    main()