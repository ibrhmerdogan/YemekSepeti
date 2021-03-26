from selenium import webdriver
from db import ctiyAddData

url = "https://www.yemeksepeti.com/sehir-secim"
driver_path = "C:\\Users\\Asus\\Desktop\\chromedriver.exe";
webBrowser = webdriver.Chrome(driver_path)
webBrowser.get(url)
cityAll = webBrowser.find_elements_by_css_selector("div[class='cityPlatesContainer']>a")
for i in cityAll:
    try:
        cityNo=i.find_element_by_class_name("plateNo").text
        cityName=i.find_element_by_class_name("name").text
        cityURL = i.get_attribute("href")
        ctiyAddData._AddData(cityName, cityNo, cityURL)
    except:
        print("KKTC")