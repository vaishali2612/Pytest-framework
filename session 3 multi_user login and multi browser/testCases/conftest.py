import pytest
from selenium import webdriver


@pytest.fixture
def demo_fixture():
    print(f"\nThis is demo fixture this will run first that means before test case")  # before testcase
    yield # Logic behind this is like it is going to check our main method or
    # you can say test case execution is completed or not if the execution of our our actual test case is completed after completion of it, it will execute below code .
    print(f"\nThis is demo fixture this will run after test case")
    """
    Browser Open
    yield
    Browser Close
    """

# @pytest.fixture
# def browser_setup():
#     print("\nThis is Browser setup")
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()
#     print("\nThis is Browser teardown")
#

# Python -v -s --browser firefox


def pytest_addoption(parser):
    parser.addoption("--browser")
# Here we are going to add - - browser is a command line argument which is user define or custom argument you can say.

# --browser chrome
# --browser firefox
# --browser edge

@pytest.fixture
def browser_setup(request):
    browser = request.config.getoption("--browser") # we are going to share --browser value at the time of execution(pytest command)
    if browser == "chrome":
        print("Launching Chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Launching Edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Launching chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# Use Name --> CredenceTest_5005@credence.in
# Password --> Password@123

@pytest.fixture(params=[
    ('CredenceTest_5005@credence.in', 'Password@123', 'login_pass'),
    ('CredenceTest_50051@credence.in', 'Password@123', 'login_fail'),
    ('CredenceTest_5005@credence.in', 'Password@1232', 'login_fail'),
    ('CredenceTest_50051@credence.in', 'Password@1232', 'login_fail')
])
def credkart_login_data(request):
    return request.param