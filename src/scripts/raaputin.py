from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from markdownify import markdownify as md
import os
from urllib.parse import urlparse
import re as re
import threading

import urllib

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

driver.close()

for link in links:
    print(link)
    page:requests.Response = requests.get(link)
    html = page.text
    mdd = md(html)
    try:
        ddd = mdd.rsplit(""" --ricos-custom-p-font-weight: inherit;
 --ricos-custom-p-font-size: 18px;
 --ricos-custom-p-line-height: 1.5;
 }""")[1]
    except:
        ddd =mdd
    fff = ddd
    print(fff)
    parsed = urllib.parse.unquote(link).split("/")[-1]
    kaka = fff.replace(r"""* [Ajankohtaista](https://www.huhuu.news/blog/categories/ajankohtaista)
    [toimitus@huhuu.news](mailto:toimitus@huhuu.news)

* [![Instagram]()](https://www.instagram.com/huhuu.news/)
* [![YouTube]()](https://www.youtube.com/channel/UCAAg6JGz08V5XoFkTcEQOtg)
bottom of page

 window.firstPageId = 'jykqx'
 window.bi.sendBeat(12, 'Partially visible', {pageId: window.firstPageId})
 if (window.requestCloseWelcomeScreen) {
 window.requestCloseWelcomeScreen()
 }
 if (!window.\_\_browser\_deprecation\_\_) {
 window.fedops.phaseStarted('partially\_visible', {paramsOverrides: { pageId: firstPageId }})
 }






{"appsWarmupData":{},"platform":{"ssrPropsUpdates":[],"ssrStyleUpdates":[],"ssrStructureUpdates":[]},"ooi":{"failedInSsr":{}}}""","")
    print(f"{parsed}.md")
    ffff = f"""---\nlayout: "../../layouts/NewsLayout.astro"\n---{kaka}"""
    faa= open(f"{parsed}.md","x")
    print(faa)
    faa.write(ffff)
    faa.close()
