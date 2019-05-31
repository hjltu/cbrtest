"""
browser.py
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
#options.add_argument('--headless')

class Browser(object):


    driver = webdriver.Firefox(options=options)
    #driver.implicitly_wait(33)
    driver.set_page_load_timeout(33)
    #driver.maximize_window()

    def close(context):
        context.driver.close()


class Google(Browser):

    def __init__(self):
        self.search = None
        self.elem = None

    def open_url(self, address):
        self.driver.get(address)

    def check_search(self, name):
        self.search = self.driver.find_element_by_name(name)
        return self.search

    def fill_search_bar(self, text):
        self.search.send_keys(text)
        return self.search

    def click_search(self):
        self.search.send_keys(Keys.RETURN)

    def find_element(self, url=None, text=None, byid=None, classname=None):
        try:
            if url:
                self.elem = self.driver.find_element_by_xpath('//a[@href="'+url+'"]')
            if text:
                self.elem = self.driver.find_element_by_link_text(text)
            if byid:
                self.elem = self.driver.find_element_by_id(byid)
            if classname:
                self.elem = self.driver.find_element_by_class_name(classname)
        except:
            return
        return self.elem

    def click_link(self, pause):
        try:
            self.elem.click()
            time.sleep(pause)
        except Exception as e:
            return "ERR"+str(e)


class Cbr(Google):

    def __init__(self):
        #self.elem = None
        super(Cbr, self).__init__()

    def check_current_url(self):
        return self.driver.current_url

    def write_text(self, elem, text):
        self.find_element(byid=elem)
        self.elem.send_keys(text)

    def save_text(self, name):
        self.search = self.find_element(byid=name).text


    def compare_text(self, name):
        self.find_element(byid=name)
        if self.search == self.elem.text:
            return "ERR"

    def take_screenshot(self, name):
        directory = 'img/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.driver.save_screenshot(directory+name)
