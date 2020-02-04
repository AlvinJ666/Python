import numpy as np
import array
import requests
import json
from datapackage import Package

class Data:
    def getCurrencyCodeJson():
        link="https://openexchangerates.org/api/currencies.json"
        url=requests.get(link)
        data=url.json()
        return data

    def getCurrencyJson():
        link="http://data.fixer.io/api/latest?access_key=c0eef8213552cf4d64b695471d6a7161&format=1"
        url=requests.get(link)
        data=url.json()
        return data
    
