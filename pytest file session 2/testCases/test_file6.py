import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Test006:

    @pytest.mark.web # @pytest.mark.group_name
    @pytest.mark.regression # @pytest.mark.group_name
    @pytest.mark.smoke
    @pytest.mark.skip
    def test_Google_Search_013(self, browser_setup):
        driver = browser_setup
        driver.get("https://www.google.com/")

        # # Search Box
        # search_box = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
        # search_box.send_keys("Credence IT, Pune", Keys.ENTER)
        #
        # time.sleep(2)
        #
        # # Search_Button
        # search_button = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
        # search_button.click()
        #
        # # open site
        # site_link = driver.find_element(By.XPATH, "//span[normalize-space()='Website']")
        # site_link.click()
        #
        # driver.quit()

    @pytest.mark.web # @pytest.mark.group_name
    @pytest.mark.regression # @pytest.mark.group_name
    def test_Contact_Search_014(self, browser_setup):
        driver = browser_setup
        driver.get("https://credence.in/")

        call_button = driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']")
        call_button.click()

        contacts_count = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[2]/a")
        print(f" len(contacts_count) -- >{len(contacts_count)} ")

        contact_list = []
        for i in range(1, (len(contacts_count) + 1)):
            contact = driver.find_element(By.XPATH, f"/html[1]/body[1]/div[5]/div[1]/div[2]/a[{i}]").text
            contact_list.append(contact)

        print(f"contact_list-->{contact_list}")

        num1 = '+91 8237916162'
        if num1 in contact_list:
            print(f"{num1}-->Number found")
        else:
            print(f"{num1}-->Number not found")
            assert False



        driver.quit()