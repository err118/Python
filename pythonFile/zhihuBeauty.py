import re

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zhihu.com/question/34946694")
result_raw = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')
content_list = result_raw.select("noscript")

for content in content_list:
    result = BeautifulSoup(content.string, 'lxml')
    imgs = result.select('img')
    for img in imgs:
        with open('img.txt', 'a', encoding='utf-8') as f:
            f.write(img['src'] + '\n')
print("fetch --->>> end")
