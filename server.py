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

import scraper
import sequent

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

        text = initialize_text(elements)
        return render_template('index.html', text=text)


def initialize_text(elements):
    time_passed,result=sequent.menu(*elements)
    text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n"
    text+="Execution Time= "+str(time_passed)+"\n\n"
    print(result)
    for i in result:
        text+=i
    return text




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
