"""Replay each URL on a list through the replay proxy, and gather results."""

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
import argparse
from multiprocessing import Process
from miproxy import proxy


def main():
    """Entry function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('server',
                        help="specify the webarchive server (arquivo.pt)")

    parser.add_argument('urls_list',
                        help="specify the txt file to read urls list")

    parser.add_argument('prefix', help="specify the wayback prefix to build the url query")

    args = parser.parse_args()

    display = Display(visible=0, size=(1024, 768))
    display.start()

    PROXY = "localhost:8080"

    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "noProxy": None,
        "proxyType": "MANUAL",
        "autodetect": False
    }

    display = Display(visible=0, size=(1024, 768))
    display.start()

    browser = webdriver.Firefox(
	firefox_binary = webdriver.firefox.firefox_binary.FirefoxBinary(log_file = open('/tmp/selenium.log','a')))

    browser.set_page_load_timeout(60)

    f = open(args.urls_list)

    for line in f.readlines():
        try:
	    #example of prefixs
            #browser.get('http://' + args.server +
            #            '/noFrame/replay/20141122132815/' + line)
            #browser.get('http://' + args.server + '/wayback/20141122132815/' + line)
	    browser.get('http://' + str(args.server) + str(args.prefix) + str(line)

            time.sleep(2)
        except TimeoutException, e:
            print e
        except UnexpectedAlertPresentException, e:
            print e
        except Exception, e:
            print e

    browser.quit()
    display.stop()

if __name__ == '__main__':
    main()
