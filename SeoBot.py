from selenium   import webdriver

#HOST
HOST = "http://www.google.com"

#CSS SELECTOR


class SeoBOt:

    def __init__(self):
        self._driver = webdriver.Chrome('./chromedriver')

    def search(self):
        self._driver.get(HOST)
        inputElement = driver.find_element_by_name("q")


def main():
    bot = SeoBOt()
    bot.search()

if __name__ == "__main__":
    main()
