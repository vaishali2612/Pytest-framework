import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test005:

    @pytest.mark.web # @pytest.mark.group_name
    @pytest.mark.regression # @pytest.mark.group_name
    @pytest.mark.smoke
    def test_Credkart_login_011(self, browser_setup):
        driver = browser_setup
        driver.get("https://automation.credence.in/login")
        # Enter Email
        email = driver.find_element(By.ID, "email")
        email.send_keys("CredenceTest_5005@credence.in")

        # Enter Password
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password@123")

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
        except:
            driver.save_screenshot("Login_failure_screenshot.png")
            print("Login Failure")
            assert False

        driver.quit()

    @pytest.mark.web # @pytest.mark.group_name
    @pytest.mark.regression # @pytest.mark.group_name
    @pytest.mark.smoke
    def test_Credkart_CheckOut_012(self, browser_setup):
        driver = browser_setup
        driver.get("https://automation.credence.in/login")
        # Enter Email
        email = driver.find_element(By.ID, "email")
        email.send_keys("CredenceTest_5005@credence.in")

        # Enter Password
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password@123")

        # Click on login button
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        login_button.click()

        # Click on "Apple macbook Pro"
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()

        # Click on add to cart button
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # Click Proceed to check out
        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()

        # Enter first name
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Credence")

        # Enter Last name
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Test")

        # Enter Phone
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")

        # Enter address
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Kharadi, Pune, Maharashtra, 411013")

        # Enter Zip Code
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411013")

        # Select State
        state_drop_down = Select(driver.find_element(By.ID, "state"))
        state_drop_down.select_by_index(1)

        # Owner Name
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Credence")

        # Cvv
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("257")

        # Enter Card Details
        card_number = driver.find_element(By.XPATH, "//input[@id='cardNumber']")
        card_number.send_keys("5281")
        card_number.send_keys("0370")
        card_number.send_keys("4891")
        card_number.send_keys("6168")

        # card number : 5281 0370 4891 6168
        # cvv : 043

        # Select Year
        Year_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        Year_dropdown.select_by_visible_text("2026")

        # Select Month
        month_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month_dropdown.select_by_visible_text("May")

        # Click on continue Checkout
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()

        try:
            print(driver.find_element(By.XPATH, "//h1[normalize-space()='Thank you.']").text)
            print(driver.find_element(By.CSS_SELECTOR, "p[class='w-lg-50 mx-auto']").text)
            print("Product Checkout successful")
        except:
            print("Product Checkout Failure")
            assert False, "Product Checkout Failure"