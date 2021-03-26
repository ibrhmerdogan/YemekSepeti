import time
from idlelib import window

import body as body
import document as document
from selenium import webdriver
from db import resLinkAddData
from db import searchText
from db import ctiySelectData
#url = selectData._SelectData()

driver_path = "C:\\Users\\Asus\\Desktop\\chromedriver.exe";
webBrowser = webdriver.Chrome(driver_path)

cityURL= ctiySelectData._SelectData()
for j in range(len(cityURL)):
    url = cityURL[j][0] +"/restoran-arama"
    plateNo = cityURL[j][1]
    try:
        if url is not None:
            webBrowser.get(url)
            height = webBrowser.execute_script("return document.documentElement.scrollHeight")
            height_new = 0
            while height != height_new:
                webBrowser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(4)
                height = height_new
                height_new = webBrowser.execute_script("return document.documentElement.scrollHeight")

            cityAll = webBrowser.find_elements_by_css_selector("div[class='ys-reslist-items']>div")
            x = 0
            for i in cityAll:
                main = i.find_element_by_class_name("restaurant-main-info")
                head = main.find_element_by_class_name("head")
                deliveryTime = head.get_attribute("data-deliverytime")
                headText = head.text
                newORold = searchText._searchFunction(headText,"YENİ")
                headRate = headText[:3]
                link = head.find_element_by_css_selector("div[class='restaurant-display-name']>a")
                resURL = link.get_attribute("href")
                resStatus = link.get_attribute("class")
                openORClosed = searchText._searchFunction(resStatus, "closedRestaurant")
                resName = link.text
                resLinkAddData._AddData(plateNo,newORold,openORClosed,deliveryTime,headRate,resURL,headText,resStatus,resName)
                x = x+1
            print(x)
        print(plateNo)
    except:
        print(plateNo  +" hata aldı ")

