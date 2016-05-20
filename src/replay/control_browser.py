"""Replay each URL on a list through the replay proxy, and gather results."""

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

    args = parser.parse_args()

    PROXY = "localhost:8080"

    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "noProxy": None,
        "proxyType": "MANUAL",
        "autodetect": False
    }

    # Process(target=proxy.main())

    browser = webdriver.Firefox()

    browser.set_page_load_timeout(10)

    f = open(args.urls_list)

    for line in f.readlines():
        try:
            browser.get('http://' + args.server +
                        '/wayback/20141122132815/' + line)
            time.sleep(2)
        except TimeoutException, e:
            print e
        except UnexpectedAlertPresentException, e:
            print e
        except Exception, e:
            print e

    #p.terminate()


if __name__ == '__main__':
    main()
