
from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions        import NoSuchElementException

from datetime       import datetime
from fake_useragent import UserAgent

import argparse
import time


#HOST
HOST = "http://www.google.com"

#CSS SELECTORS

#NAME SELECTORS
GOOGLEINPUT = "q"

#ID SELECTORS
RESULTS = "rso"

# JAVASCRIPT COMMANDS
SCROLL_UP = "window.scrollTo(0, 0);"
SCROLL_DOWN = "window.scrollTo(0, 200);"


class SeoBOt:

    def __init__(self):
        ua = UserAgent()
        #Set chrome_options
        opts = Options()
        randomuser = "user-agent=" + ua.random
        opts.add_argument(randomuser)
        self._driver = webdriver.Chrome('./chromedriver', chrome_options=opts)
        agent = self._driver.execute_script("return navigator.userAgent")
        self.printWithLog('{}\n'.format(agent))

    def search(self, keywords):
        self._driver.get(HOST)
        inputElement = self._driver.find_element_by_name(GOOGLEINPUT)
        inputElement.send_keys(keywords)
        inputElement.submit()

    def getResults(self, urlsite):
        i = 0
        res = self._driver.find_elements_by_class_name("g")
        for div in res:
            try:
                url = div.find_element_by_tag_name('cite')
                if urlsite in url.text:
                    link = div.find_element_by_tag_name('h3')
                    self._driver.execute_script(SCROLL_DOWN)
                    link.click()
                    return

            except NoSuchElementException:
                pass

    def quit(self):
        self._driver.quit()

    def crawl(self, keywords, urlsite):
        self.search(keywords)
        self.getResults(urlsite)
        self.quit()

    def printWithLog(self, variable):
        print ("[{}]    ".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), end='')
        print (variable)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('website', metavar='w',
                        help='Website url')
    parser.add_argument('keywords', metavar='k',
                        help='keywords to search in Google')

    args = parser.parse_args()

    while True:
        bot = SeoBOt()
        bot.crawl(args.keywords, args.website)

if __name__ == "__main__":
    main()
