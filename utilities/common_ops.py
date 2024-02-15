import csv
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_cases import conftest
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:/Users/daniels/PycharmProjects/mcdonaldsFrontAutomation/configuration/data.xml').getroot()
    return root.find(".//" + node_name).text

def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data),row)
        return data

def csv_to_dictionary(file_name):
    """
    this method takes a CSV file and makes a dictionary out of it.
    the first value of each line is a key and the rest of the values in the same line are that key's value in a form of a list.
    example: birds, hawk, dodo, flamingo >>> {birds : [hawk, dodo, flamingo]}
    """
    data = {}
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1:]
        return data


def wait(for_element, elem):
    wait_time = 10
    if for_element == 'element exists':
        WebDriverWait(conftest.driver, wait_time).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element displayed':
        WebDriverWait(conftest.driver, wait_time).until(EC.visibility_of_element_located((elem[0], elem[1])))
    elif for_element == 'element to be clickable':
        WebDriverWait(conftest.driver, wait_time).until(EC.element_to_be_clickable((elem[0], elem[1])))
    elif for_element == 'presence of element':
        WebDriverWait(conftest.driver, wait_time).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element invisible':
        WebDriverWait(conftest.driver, wait_time).until(EC.invisibility_of_element_located((elem[0], elem[1])))
    elif for_element == 'visibility of all elements':
        WebDriverWait(conftest.driver, 60, poll_frequency=1, ignored_exceptions=[StaleElementReferenceException]).until(EC.visibility_of_all_elements_located((elem[0], elem[1])))
    elif for_element == 'staleness of element':
        WebDriverWait(conftest.driver, wait_time).until(EC.staleness_of((elem[0], elem[1])))
    elif for_element == 'text to be present':
        WebDriverWait(conftest.driver, wait_time).until(EC.text_to_be_present_in_element((elem[0], elem[1])))


#Enum for selecting displayed elements or existing elelemnts
class For:
    ELEMENT_EXISTS = 'element exists'
    ELEMENT_DISPLAYED = 'element displayed'
    ELEMENT_TO_BE_CLICKABLE = 'element to be clickable'
    PRESENCE_OF_ELEMENT = 'presence of element'
    ELEMENT_INVISIBLE = 'element invisible'
    ALL_ELEMENTS_VISIBLE = 'visibility of all elements'
    STALENESS_OF = 'staleness of element'
    TEXT_TO_BE_PRESENT = 'text to be present'


class By:
    USER = 'user'
    INDEX = 'index'


def get_timestamp():
    return time.time()

def lower_strip_list(list):
    for x in range(len(list)):
        list[x] = list[x].lower().strip()
    return list