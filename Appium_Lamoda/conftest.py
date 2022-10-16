import pytest
from appium import webdriver
import os


def pytest_addoption(parser):
    parser.addoption('--OS_name', action='store', default=None,
                           help="Choose device: android or ios")


@pytest.fixture(scope="function")
def drivers(request):
    OS_name = request.config.getoption("--OS_name")

    drivers = None
    
    if OS_name == 'android':
        caps = {
            "platformName":"Android",
            "app":os.path.abspath("apk\\com.lamoda.lite_4.17.0_401700.apk")
        }
        
        drivers = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        
    else:
        print('\nCheck if the:\n --OS_name:android or ios values ​​are entered correctly')
 
    yield drivers
    print("\nquit device..")
    drivers.quit()

