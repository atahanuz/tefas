import time

from flask import Flask, render_template, request
import datetime

import datetime
import time

import requests
from bs4 import BeautifulSoup
import re
import sys
from multiprocessing import Manager
import concurrent.futures

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():


    if request.method == 'GET':
        #text = initialize_text(elements)
        text="Enter ETF names seperated by space. If you don't enter anything, default ETFs will be used."
        text+= "\nExample: MAC AFT IPJ TCD TKF AEH"
        return render_template('index.html', text=text)

    if request.method == 'POST':
        elements = request.form.get('elements').split(' ')
        elements = [element.upper() for element in elements]
        if elements==[""]:
            elements = ["MAC", "AFT", "IPJ", "TCD", "TKF", "AEH"]

        time_passed, result = menu(*elements)
        text=result
        return render_template('index.html', text=text)


def initialize_text(elements):
    time_passed,result=menu(*elements)
    text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n"
    text+="Execution Time= "+str(time_passed)+"\n\n"
    print(result)
    for i in result:
        text+=i
    return text


def menu(*arguments):
    print("started scraping")
    start_time = time.time()
    if arguments is None:
        arguments = sys.argv[1:]

    with Manager() as manager:
        results = manager.list(range(len(arguments)))
        with concurrent.futures.ThreadPoolExecutor() as executor:
            counter=0
            tasks=[]
            for arg in arguments:
                tasks.append((counter,arg, results))
                counter+=1
            executor.map(worker, tasks)

        results = list(results)

    time_passed = time.time()-start_time
    return time_passed, results


def worker(task):
    counter,name, results = task
    finaltext = ""
    baseurl = "https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod="

    url = baseurl + name


    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
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
    results[counter]= finaltext



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
