import time

import allure
import pytest

from utilities.common_ops import get_data
#from workflows.app_flows import App_Flows as flow
from extensions.verifications import Verifications as ver



@pytest.mark.usefixtures('init_mobile_driver_adidas')
class Test_Mcdonalds_App:

    def setup_method(self):
        pass

    def test1(self):
        pass