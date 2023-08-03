import datetime
import time

import requests
from bs4 import BeautifulSoup
import re
import sys

def main(*arguments):
    finaltext = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n"
    baseurl="https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod="

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

        name_search = re.search('Analiz(.*?)Son', all_text)
        name = name_search.group(1) if name_search else 'Unknown'

        increment_search = re.search('\)%\s*(.*?)Pay', all_text)
        increment = increment_search.group(1).replace(',', '.') if increment_search else '0.0'

        price_search = re.search('t \(TL\)\s*(.*?)Günlük', all_text)
        price = price_search.group(1).replace(',', '.') if price_search else '0.0'

        #convert to float
        price = float(price)
        increment = float(increment)

        #merge argument, price and increment in a string.
        result = f'FON= {name}\nKOD= {add}\nPRICE= {price}\nCHANGE= {increment}\n\n'
        finaltext += result

    return finaltext



if __name__ == '__main__':
    start_time = time.time()
    text=main("MAC", "AFT", "IPJ", "TCD", "TKF", "AEH")
    print("--- %s seconds ---" % (time.time() - start_time))
    print(text)