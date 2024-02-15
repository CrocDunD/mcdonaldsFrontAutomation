import allure
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from test_cases import conftest


class Ui_Actions:
    @staticmethod
    @allure.step('Click')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('Send keys')
    def update_text(elem: WebElement, value):
        elem.send_keys(value)

    @staticmethod
    @allure.step('Mouse hover and click')
    def mouse_hover_and_click(elem1: WebElement, elem2: WebElement):
        ActionChains(conftest.driver).move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Mouse hover')
    def mouse_hover(elem1: WebElement):
        ActionChains(conftest.driver).move_to_element(elem1).perform()

    @staticmethod
    @allure.step('Right click')
    def right_click(elem: WebElement):
        ActionChains(conftest.driver).context_click(elem).perform()

    @staticmethod
    @allure.step('Drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        ActionChains(conftest.driver).drag_andDrop(elem1,elem2).perform()

    @staticmethod
    @allure.step('Clear text')
    def clear(elem: WebElement):
        elem.clear()

    @staticmethod
    def multiple_clicks(list):
        ActionChains(conftest.driver).click(list[0]).click(list[1]).perform()

    @staticmethod
    def click_mobile_keyboard_key(key):
        if key == 'enter':
            conftest.driver.press_keycode(AndroidKey.ENTER)
        elif key == 'search':
            conftest.driver.press_keycode(AndroidKey.SEARCH)
        elif key == 'back':
            conftest.driver.press_keycode(AndroidKey.BACK)

    @staticmethod
    def swipe():
        conftest.driver.swipe(100,1250,100,0,300)

class Key:
    ENTER = 'enter'
    SEARCH = 'search'
    BACK = 'back'


