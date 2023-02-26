from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from markdownify import markdownify as md
import os
from urllib.parse import urlparse
import re as re

SCROLL_PAUSE_TIME = 2
links: str = []
driver = webdriver.Firefox()
driver.get("http://www.huhuu.news/blog")
time.sleep(2)
i = 0
while i < 5:
    i = i + 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

elems = driver.find_elements(By.CLASS_NAME ,"O16KGI")
for elem in elems:
    links.append(elem.get_attribute("href"))


for link in links:
    print(link)
    page:requests.Response = requests.get(link)
    html:str = page.text
    md: str = md(html)
    parsed = re.search("(?<=https:\/\/www.huhuu.news\/blog\/posts\/)(?s)(.*$)", urlparse(link).path)
    os.open(f"{parsed}.md", os.O_CREAT | os.O_WRONLY)
    os.write(link, md)
