#encoding:utf-8

from selenium.common.exceptions import StaleElementReferenceException


class TextNotEmptyInElement(object):

    def __init__(self, xpath):
        self.xpath = xpath

    def __call__(self, driver):
        try :
            element_text = driver.find_element_by_xpath(self.xpath).text
            return element_text != ''
        except StaleElementReferenceException:
            return False

class ElementLocated(object):

    def __init__(self, xpath):
        self.xpath = xpath

    def __call__(self, driver):
        count = len(driver.find_elements_by_xpath(self.xpath))
        
        return count > 0

