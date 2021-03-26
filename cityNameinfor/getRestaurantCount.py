import time
from idlelib import window

import body as body
import document as document
from selenium import webdriver
from db import resCountAddData
from db import searchText
from db import ctiySelectData
#url = selectData._SelectData()

driver_path = "C:\\Users\\Asus\\Desktop\\chromedriver.exe";
webBrowser = webdriver.Chrome(driver_path)

cityURL= ctiySelectData._SelectData()
for j in range(len(cityURL)):
    url = "https://www.yemeksepeti.com/" + cityURL[j][0]+"#ors:false"
    name =cityURL[j][1]
    plateNo ='0606'
    try:
        if url is not None:
            webBrowser.get(url)
            time.sleep(2)
            cityAll = webBrowser.find_element_by_css_selector("div[class='ys-result-count']>p>b>span")
            count = cityAll.text
            reg_date = time.localtime()
            resCountAddData._AddData(count,plateNo,reg_date,name)
    except:
        print(url  +" hata aldı ")

