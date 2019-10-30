#!/usr/bin/env python
import time

from selenium import webdriver

if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.get('https://www.gousto.co.uk/cookbook/all-recipes')

    def click_link():
        while (driver.find_element_by_link_text("See more")):
            time.sleep(2)
            driver.find_element_by_link_text("See more").click()

    try:
        click_link()
    except:
        if (driver.find_element_by_class_name('sumome-react-wysiwyg-close-button')):
            driver.find_element_by_class_name('sumome-react-wysiwyg-close-button').click()
            click_link()


