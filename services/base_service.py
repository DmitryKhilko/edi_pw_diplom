import json

import requests

from data.file_name_data import FILENAME_API_PERSON_ID
from data.url_data import PERSONS_GET_END_POINT, PERSON_CREATE_END_POINT, CSRF_END_POINT, LOGIN_END_POINT
from helper.files import FilesWork
from settings import BASE_URL


class BaseService:

    @staticmethod
    def get_csrftoken():
        url = BASE_URL + CSRF_END_POINT
        response = requests.get(url)
        csrftoken = response.cookies.get('csrftoken')
        status_code = response.status_code
        return csrftoken, status_code

    @staticmethod
    def authorization(csrftoken: str, user: tuple):
        url = BASE_URL + LOGIN_END_POINT
        payload = json.dumps({
            'login': user[1],
            'password': user[2]
        })
        headers = {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
            'Cookie': f'csrftoken={csrftoken}'
        }
        response = BaseService.post(url, payload, headers)
        # Переприсваиваем значения cookies переменным,
        # так как после POST запроса изменился csrftoken и добавился sessionid
        csrftoken = response.cookies.get('csrftoken')
        sessionid = response.cookies.get('sessionid')
        status_code = response.status_code
        reason = response.reason
        result = response.json()
        return csrftoken, sessionid, status_code, reason, result

    @staticmethod
    def get(url: str, headers: dict):
        headers = headers
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(url: str, payload, headers: dict):
        payload = payload
        headers = headers
        response = requests.post(url, headers=headers, data=payload)
        return response

    @staticmethod
    def patch(url: str, payload, headers: dict):
        payload = payload
        headers = headers
        response = requests.patch(url, headers=headers, data=payload)
        return response

    @staticmethod
    def delete(self):
        pass

    @staticmethod
    def get_persons(csrftoken: str, sessionid: str):
        url = BASE_URL + PERSONS_GET_END_POINT
        headers = {
            'Cookie': f'csrftoken={csrftoken}; sessionid={sessionid}'
        }

        response = BaseService.get(url, headers)
        status_code = response.status_code
        reason = response.reason
        result = response.json()

        return status_code, reason, result

    @staticmethod
    def add_person(csrftoken: str, sessionid: str, data: tuple):
        url = BASE_URL + PERSON_CREATE_END_POINT

        payload = json.dumps({
            'first_name': data[0],
            'last_name': data[1],
            'patronymic': data[2],
            'sex': data[3],
            'birth_date': data[4],
            'phone': data[5],
            'email': data[6],
            'key_id': data[7],
            'card_id': data[8]
        })
        headers = {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
            'Cookie': f'csrftoken={csrftoken}; sessionid={sessionid}'
        }

        response = BaseService.post(url, payload, headers)
        status_code = response.status_code
        reason = response.reason
        result = response.json()

        # Если создалась запись физического лица в базе данных, записываем personal_id в файл
        # для последующего удаления физического лица из БД
        if status_code == 201:
            FilesWork.write_file(FILENAME_API_PERSON_ID, result['person_id'])

        return status_code, reason, result



