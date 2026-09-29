import time

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test004:

    @pytest.mark.web # @pytest.mark.group_name
    @pytest.mark.smoke
    @pytest.mark.regression # @pytest.mark.group_name
    @pytest.mark.sanity
    @pytest.mark.flaky(reruns = 1, rerun_delay = 0)
    def test_Credkart_Registration_009(self, browser_setup):
        driver = browser_setup
        driver.get("https://automation.credence.in/")
        # Click on Register link
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[4]/a").click()

        # Enter Name
        driver.find_element(By.ID, "name").send_keys("Credence")

        # Enter Email
        driver.find_element(By.ID, "email").send_keys("CredenceTest_5005@credence.in")

        # Enter Password
        driver.find_element(By.ID, "password").send_keys("Password@123")

        # Enter Confirm Password
        driver.find_element(By.ID, "password-confirm").send_keys("Password@123")

        # Click Register Button
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        # Verify Registration
        try:
            #driver.save_screenshot("Registration_success_screenshot.png")
            # Click on menu Button
            driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/a").click()
            # Click on Logout link
            driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
            print("Registration Success")
        except:
            driver.save_screenshot("Registration_failure_screenshot.png")
            print("Registration Failure")
            assert False

        driver.quit()

    @pytest.mark.web # @pytest.mark.group_name
    @pytest.mark.regression # @pytest.mark.group_name
    @pytest.mark.sanity
    def test_Credkart_Registration_010(self, browser_setup):
        driver = browser_setup
        driver.get("https://automation.credence.in/")

        # Click on Register link
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[4]/a").click()

        name_data = Faker().name()
        print(f"name_data-->{name_data}")

        email_data = Faker().email()
        print(f"email_data-->{email_data}")

        # Enter Name
        driver.find_element(By.ID, "name").send_keys(name_data)

        # Enter Email
        driver.find_element(By.ID, "email").send_keys(email_data)

        # Enter Password
        driver.find_element(By.ID, "password").send_keys("Password@123")

        # Enter Confirm Password
        driver.find_element(By.ID, "password-confirm").send_keys("Password@123")

        # Click Register Button
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        # Verify Registration
        try:
            #time.sleep(5)
            driver.save_screenshot("Registration_success_screenshot.png")
            # Click on menu Button
            driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/a").click()
            # Click on Logout link
            driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
            print("Registration Success")
        except:
            driver.save_screenshot("Registration_failure_screenshot.png")
            print("Registration Failure")
            assert False

        driver.quit()
