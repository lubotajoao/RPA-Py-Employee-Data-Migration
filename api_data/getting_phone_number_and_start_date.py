import requests


def getting_phone_number(url, employee_id):
    employee_api = url + str(employee_id)
    response_api = requests.get(employee_api)
    load_data = response_api.json()
    phone_number = (load_data['phoneNumber'])

    return phone_number


def getting_start_date(url, employee_id):
    employee_api = url + str(employee_id)
    response_api = requests.get(employee_api)
    load_data = response_api.json()
    start_date = (load_data['startDate'])

    return start_date
