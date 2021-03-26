import time
from selenium import webdriver
from db import fourCityAddData
from db import searchText
from db import ctiySelectData

driver_path = "C:\\Users\\Asus\\Desktop\\chromedriver.exe";
webBrowser = webdriver.Chrome(driver_path)

cityURL= ctiySelectData._SelectData()
for j in range(len(cityURL)):
    url = cityURL[j][0] +"/restoran-arama"
    plateNo = cityURL[j][1]
    try:
        if url is not None:
            webBrowser.get(url)
            cityAll = webBrowser.find_elements_by_css_selector("select[class='form-control area-selector select2-hidden-accessible']>optgroup>option")
            for i in cityAll:
                name = i.text
                url = i.get_attribute("data-url")
                fourCityAddData._AddData(plateNo,url,1,name)
            time.sleep(4)
    except:
        print(plateNo  +" hata aldı ")

