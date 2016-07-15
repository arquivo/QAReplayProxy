"""Replay each URL on a list through the replay proxy, and gather results."""

import argparse
import threading
import time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException

from miproxy import *


def launchProxy(filter_path):
    thread = threading.Thread(target=proxy.main, args=(filter_path,))
    thread.daemon = True
    thread.start()


def main():
    """Entry function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('server',
                        help="specify the webarchive server (arquivo.pt)")

    parser.add_argument('urls_list',
                        help="specify the txt file to read urls list")

    parser.add_argument('prefix',
                        help="specify the wayback prefix to build the url query (example: /wayback/20141122132815)")
    parser.add_argument('liveleaks_prefix',
                        help="specify the prefix in which request that dont have it should be considered liveleaks (example: '.*(\/wayback\/).*')")

    args = parser.parse_args()

    display = Display(visible=0, size=(1024, 768))
    display.start()

    launchProxy(args.liveleaks_prefix)

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
        firefox_binary=webdriver.firefox.firefox_binary.FirefoxBinary(log_file=open('/tmp/selenium.log', 'a')))

    browser.set_page_load_timeout(60)

    f = open(args.urls_list)

    for line in f.readlines():
        try:
            # example of prefixes
            # browser.get('http://' + args.server +
            #            '/noFrame/replay/20141122132815/' + line)
            browser.get('http://' + str(args.server) + str(args.prefix) + str(line))

            time.sleep(2)
        except TimeoutException, e:
            print e
        except UnexpectedAlertPresentException, e:
            print e
        except Exception, e:
            print e

    browser.quit()
    display.stop()

    proxy.report_metrics()

if __name__ == '__main__':
    main()
