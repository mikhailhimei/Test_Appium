import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction 


class BasePage():
    def __init__(self, drivers):
        self.drivers = drivers
        self.drivers.implicitly_wait(40)

    def screenshot(self):
        try:
            self.drivers.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
        except:
            return False
        return True
    
    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.drivers, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.drivers, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_hide_keyboard(self):
        self.drivers.hide_keyboard()

    def is_back(self):
        self.drivers.back()

    def start_search(self):
        try:
            self.drivers.execute_script("mobile:performEditorAction",{'action':'search'})

        except TimeoutException:
            return False
            
        return True


    def scroll_element(self, element, xPos=300, yPos=1000):
        try:
            actions = TouchAction(self.drivers) 
            actions.long_press(element)
            actions.move_to(None,xPos, yPos)
            actions.release()
            actions.perform()

        except TimeoutException:
            return False
            
        return True
