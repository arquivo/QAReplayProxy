from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time

PROXY = "localhost:8080"

webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "noProxy": None,
    "proxyType": "MANUAL",
    "autodetect": False
}

browser = webdriver.Firefox()

browser.set_page_load_timeout(10)


f = open('test_urls.txt')

for line in f.readlines():
    try:
        browser.get('http://arquivo.pt/wayback/20141122132815/' + line)
        time.sleep(2)
    except TimeoutException, e:
        print e
