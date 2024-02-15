import allure
import requests
from requests.auth import HTTPBasicAuth

header = {'Content-Type':'application/json'}

class Api_Actions:
    @staticmethod
    @allure.step('Sent Get Request')
    def get(path,user,password):
        response = requests.get(path, auth=HTTPBasicAuth(user,password))
        return response

    @staticmethod
    @allure.step('Extract Value From Response')
    def extract_value_from_response(response, nodes):
        extracted_values = None
        response_json = response.json()
        if len(nodes) == 1:
            extracted_values = response_json[nodes[0]]
        elif len(nodes) == 2:
            extracted_values = response_json[(nodes[0])][(nodes[1])]
        elif len(nodes) == 3:
            extracted_values = response_json[(nodes[0])][(nodes[1])][(nodes[2])]
        elif len(nodes) == 4:
            extracted_values = response_json[(nodes[0])][(nodes[1])][(nodes[2])][(nodes[3])]
        return extracted_values

    @staticmethod
    @allure.step('Sent Post Request')
    def post(path, payload, user, password):
        response = requests.post(path,json=payload,headers=header, auth=HTTPBasicAuth(user, password))
        return response

    @staticmethod
    @allure.step('Sent Patch Request')
    def put(path, payload, user, password):
        response = requests.patch(path, json=payload, headers=header, auth=HTTPBasicAuth(user, password))
        return response

    @staticmethod
    @allure.step('Sent Delete Request')
    def delete(path, user, password):
        response = requests.delete(path, auth=HTTPBasicAuth(user, password))
        return response