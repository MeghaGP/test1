from selenium import webdriver
import unittest
import os
import time
from selenium.webdriver.support.ui import Select


class ClearTripTC(unittest.TestCase):
    def setUp(self):
        dir=os.path.dirname(__file__)
        chrome_driver_path=dir+"\chromedriver.exe"
        self.driver=webdriver.Chrome(chrome_driver_path)
        self.driver.get("https://www.cleartrip.com/")
        self.driver.implicitly_wait(30)

    def test_Clear_TicketTC(self):
        self.driver.find_element_by_id('RoundTrip').click()
        #self.driver.find_element_by_xpath("//input[@id='FromTag']").clear()
        self.driver.find_element_by_xpath("//input[@id='FromTag']").send_keys("Bangalore")
        self.driver.find_element_by_xpath("//input[@id='ToTag']").send_keys("Delhi")
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_xpath("//input[@id='DepartDate']").send_keys('Sat,17 Nov,2018')
        self.driver.find_element_by_xpath("//input[@id='ReturnDate']").clear()
        self.driver.find_element_by_xpath("//input[@id='ReturnDate']").send_keys('Sun,18 Nov,2018')


        #wait.until(lambda driver: driver.find_element_by_xpath("//div[@id='ui-datepicker-div']"))
        #self.driver.find_element_by_xpath("//div[@id='ui-datepicker-div']//a[@class='ui-state-default'][text()='10']").click()  # meaning //div[@id='ui-datepicker-div']//td/a[@class='ui-state-default'][text()='10']
        self.driver.implicitly_wait(30)

        select = Select(self.driver.find_element_by_xpath("""//*[@id='Adults']"""))
        select.select_by_visible_text('3')
        time.sleep(5)
        select = Select(self.driver.find_element_by_xpath("""//*[@id='Childrens']"""))
        select.select_by_visible_text('2')
        time.sleep(5)
        select = Select(self.driver.find_element_by_xpath("""//*[@id='Infants']"""))
        select.select_by_visible_text('1')
        time.sleep(5)
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_id("MoreOptionsLink").click()

        select = Select(self.driver.find_element_by_xpath("""//*[@id='Class']"""))
        select.select_by_visible_text("First")

        self.driver.find_element_by_id("AirlineAutocomplete").send_keys("Air India(AI)")
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//*[@id='SearchBtn']").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
