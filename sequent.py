
import datetime
import subprocess
import time
import urllib.request
import http.client
import ssl
import requests
from bs4 import BeautifulSoup
import re
import sys
from multiprocessing import Manager
import concurrent.futures


def menu(*arguments):
    print("started scraping")
    start_time = time.time()
    if arguments is None:
        arguments = sys.argv[1:]


    results = []

    for name in arguments:

        finaltext = ""
        baseurl = "https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod="

        url = baseurl + name
        subprocess.run(['curl', '--tlsv1.2', 'https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod=AFT', '-o', 'output.html'])
        # parse the webpage
        with open('output.html', 'r') as f:
            contents = f.read()

        soup = BeautifulSoup(contents, "html.parser")
        all_text = ''.join(soup.stripped_strings)

        # first 1000 characters of the string
        all_text = all_text[500:800]

        name_search = re.search('Analiz(.*?)Son', all_text)
        fullname = name_search.group(1) if name_search else 'Unknown'

        increment_search = re.search('\)%\s*(.*?)Pay', all_text)
        increment = increment_search.group(1).replace(',', '.') if increment_search else '0.0'

        price_search = re.search('t \(TL\)\s*(.*?)Günlük', all_text)
        price = price_search.group(1).replace(',', '.') if price_search else '0.0'

        # convert to float
        price = float(price)
        increment = float(increment)

        # merge argument, price and increment in a string.
        result = f'KOD= {name}\nNAME= {fullname}\nPRICE= {price}\nCHANGE= {increment}\n\n'

        finaltext += result

        # add name and result to the results dictionary
        results.append(finaltext)

    time_passed = time.time() - start_time
    return time_passed, results





if __name__ == '__main__':
    start_time = time.time()
    print("started")
    #datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n"
    results=menu("MAC", "AFT", "IPJ", "TCD", "TKF", "AEH", "TPC")
    print(results)
    print("ended")




    print("--- %s seconds ---" % (time.time() - start_time))