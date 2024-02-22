import test_cases
from page_objects.app_objects.app_prom_first_banner_page import App_prom_first_banner_page



#web_front_page = None


app_prom_first_banner_page = None


class Manage_Pages:
#     @staticmethod
#     def init_web_pages():
#         #global web_front_page
#
#         #web_front_page = Front_Page(test_cases.conftest.driver)
#

    @staticmethod
    def init_app_pages():
        global app_prom_first_banner_page

        app_prom_first_banner_page = App_prom_first_banner_page(test_cases.conftest.driver)