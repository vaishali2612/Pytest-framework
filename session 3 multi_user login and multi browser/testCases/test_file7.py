import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test007:

    @pytest.mark.web # @pytest.mark.group_name
    @pytest.mark.regression # @pytest.mark.group_name
    @pytest.mark.smoke
    def test_Credkart_login_015(self, browser_setup, credkart_login_data):
        driver = browser_setup
        driver.get("https://automation.credence.in/login")
        # Enter Email
        self.email = credkart_login_data[0]
        self.password = credkart_login_data[1]
        self.expected_result = credkart_login_data[2]

        email = driver.find_element(By.ID, "email")
        email.send_keys(self.email)

        # Enter Password
        password = driver.find_element(By.ID, "password")
        password.send_keys(self.password)

        # Click on login button
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        login_button.click()

        # Verify Login
        try:
            # time.sleep(5)
            # Wait to load menu button
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@role='button']"))
                )
            driver.save_screenshot("Login_success_screenshot.png")
            # Click on menu Button
            driver.find_element(By.XPATH, "//a[@role='button']").click()
            # Click on Logout link
            driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
            print("Login Success")
            actual_result = "login_pass"
        except:
            driver.save_screenshot("Login_failure_screenshot.png")
            print("Login Failure")
            actual_result = "login_fail"

        assert actual_result == self.expected_result, f"{actual_result} != {self.expected_result}"
        driver.quit()

#>pytest -v -s  --html=HTMLReports/my_report_firefox.html --browser chrome -k "test_Credkart_login_015"