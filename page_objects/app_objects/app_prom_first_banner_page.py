from selenium.webdriver.common.by import By

x_button = (By.XPATH,"//*[@id='ivTransitionClose']")


class App_prom_first_banner_page:
    def __init__(self,driver):
        self.driver = driver

    def get_x_button(self):
        return self.driver.find_element(x_button[0],x_button[1])