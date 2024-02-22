import time

import allure
import pytest

from utilities import manage_pages as page
from extensions.ui_actions import Ui_Actions, Key
from utilities.common_ops import get_data
#from workflows.app_flows import App_Flows as flow
from extensions.verifications import Verifications as ver



@pytest.mark.usefixtures('init_mobile_driver_adidas')
class Test_Mcdonalds_App:

    def setup_method(self):
        Ui_Actions.click(page.app_prom_first_banner_page.get_x_button())
        time.sleep(5)
        pass

    def test_login_with_email(self):
        pass