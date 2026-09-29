import pytest
from selenium import webdriver


@pytest.fixture
def demo_fixture():
    print(f"\nThis is demo fixture this will run first that means before test case")  # before testcase
    yield # Logic behind this is like it is going to check our main method or you can say test case execution is completed or not if the execution of our our actual test case is completed after completion of it, it will execute below code .
    print(f"\nThis is demo fixture this will run after test case")
    """
    Browser Open
    yield
    Browser Close
    """

@pytest.fixture
def browser_setup():
    print("\nThis is Browser setup")
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    print("\nThis is Browser teardown")



