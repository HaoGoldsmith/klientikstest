import requests
#задание a - получение списка сотрудников
account_id = "c6637265cdbe"
user_id ="c35a9cedb0ce"
access_token = "730ba9573dfb6d3930ec8deefcbf8ff8"
url_empl_list = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}/t/{access_token}/m/Users/")
list_of_employees = requests.get(url_empl_list)
print(list_of_employees.json())

#функция
def list_of_employees(client):
    try:
        api_key = client.get_var_val('klientiks_api_key')
        status, result = requests.get(api_key)
        if status:
            answer = {'status': '1', 'result': True}
        else:
            answer = {'status': '0', 'error': result}
        client.get_project().increment_send_statistic()

    except Exception as e:
        answer = {'status': '0', 'error': str(e)}
    return ujson.dumps(answer, ensure_ascii=False)

#задание b - получить доступное время для записи
params_free_date = {'start_day': '2022-03-07', 'finish_day': '2022-03-07', 'service_id[]': '1210056',
        'executor_id': '120933'}
url_free_date = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}/t/{access_token}/m/availableTimes")
data_free_date = requests.get(url_free_date, params=params_free_date)
print(data_free_date.json())

#функция
def get_free_date(client,bot_variables,start_day,finish_day=None,service_id=None,executor_id=None):
    try:
        api_key = client.get_var_val('klientiks_api_key')
        if api_key:
            if not start_day:
                start_day = bot_variables.get('start_day')
                if not start_day:
                    return {'status': '0', 'error': 'Missing required variables - start_day'}
            if not finish_day:
                finish_day = bot_variables.get('finish_day')
            if not service_id:
                service_id = bot_variables.get('service_id')
            if not executor_id:
                executor_id = bot_variables.get('executor_id')
            params_free_date = {'start_day': 'start_day',
                                'finish_day': 'finish_day',
                                'service_id[]': 'service_id',
                                'executor_id': 'executor_id'}
            status, result = requests.get(api_key, params=params_free_date)
            if status:
                answer = {'status': '1', 'result': True}
            else:
                answer = {'status': '0', 'error': result}
            client.get_project().increment_send_statistic()
        else:
            answer = {'status': '0', 'error': "No api_key in 'klientiks_api_key' variable in project settings"}

    except Exception as e:
     answer = {'status': '0', 'error': str(e)}
    return ujson.dumps(answer, ensure_ascii=False)

#задание с - добавить визит для основного клиента
url_add_record = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}/t/{access_token}/m/Appointments/s/apiAdd/")
params_add_record = {'executor_id': 120933, 'service_id[]': 1210056, 'start_datetime': '2022-03-07 11:00:00', 'first_name': 'Николай', 'phone': '79111100005','subclient_name': 'Гарри','appointment_id': 11111,'living_address': 'Невский 1','birth_date': '23.02.1991'}
resp = requests.post(url_add_record, data=params_add_record)
print(requests.get(url_add_record, params=params_add_record))
print(resp.json())

#функция
def add_record(client,bot_variables,executor_id,service_id,start_datetime,first_name,phone,subclient_name=None,
                appointment_id=None,living_address=None,birth_date=None):
     try:
            api_key = client.get_var_val('klientiks_api_key')  # апи ключ в переменной проекта
            if api_key:
                if not executor_id:
                    executor_id = bot_variables.get('executor_id')
                    if not executor_id:
                        return {'status': '0', 'error': 'Missing required variables - executor_id'}
                if not service_id:
                    service_id = bot_variables.get('service_id')
                    if not service_id:
                        return {'status': '0', 'error': 'Missing required variables - service_id'}
                if not start_datetime:
                    start_datetime = bot_variables.get('start_datetime')
                    if not start_datetime:
                        return {'status': '0', 'error': 'Missing required variables - start_datetime'}
                if not first_name:
                    first_name = bot_variables.get('first_name')
                    if not first_name:
                        return {'status': '0', 'error': 'Missing required variables - first_name'}
                if not phone:
                    phone = bot_variables.get('phone')
                    if not phone:
                        return {'status': '0', 'error': 'Missing required variables - phone'}
                if not subclient_name:
                    subclient_name = bot_variables.get('subclient_name')
                if not appointment_id:
                    appointment_id = bot_variables.get('appointment_id')
                if not living_address:
                    living_address = bot_variables.get('living_address')
                if not birth_date:
                    birth_date = bot_variables.get('birth_date')
                params_add_record = {'executor_id': 'executor_id',
                                     'service_id[]': 'service_id',
                                     'start_datetime': 'start_datetime' ,
                                     'first_name': 'first_name',
                                     'phone': 'phone',
                                     'subclient_name': 'subclient_name',
                                     'appointment_id': 'appointment_id',
                                     'living_address': 'living_address',
                                     'birth_date': 'birth_date'}
                status, result = requests.post(api_key, data=params_add_record)
                if status:
                    answer = {'status': '1', 'result': True}
                else:
                    answer = {'status': '0', 'error': result}
                client.get_project().increment_send_statistic()
            else:
                answer = {'status': '0', 'error': "No api_key in 'klientiks_api_key' variable in project settings"}
     except Exception as e:
            answer = {'status': '0', 'error': str(e)}
     return ujson.dumps(answer, ensure_ascii=False)


# Задание d - добавить клиента
url_add_сlient = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}/t/{access_token}/m/Clients/")
params_add_client = {'phone': '74445550011', 'first_name': 'Иван', 'patron_name': 'Иванович', 'second_name': 'Иванов',
                     'email': 'test@test.com', 'client_groups': 'Новенький', 'living_address': 'Невский проспект, 25',
                     'sex': '1', 'appointment_confirmation_sms': '1', 'lead_source': 'бот'}
resp_client = requests.post(url_add_сlient, data=params_add_client)
print(requests.get(url_add_сlient, params=params_add_client))
print(resp_client.json())

#функция - добавить клиента
def add_new_clients(client,bot_variables,phone,first_name,patron_name=None,second_name=None,email=None,living_address=None,
                    sex=None,appointment_confirmation_sms=None,lead_source=None,client_groups=None):
        try:
                api_key = client.get_var_val('klientiks_api_key')  # апи ключ в переменной проекта
                if api_key:
                        if not phone:
                              phone = bot_variables.get('phone')
                              if not phone:
                                  return {'status': '0', 'error': 'Missing required variables - phone'}
                        if not first_name:
                            first_name = bot_variables.get('first_name')
                            if not first_name:
                                return {'status': '0', 'error': 'Missing required variables - first_name'}
                        if not patron_name:
                            patron_name = bot_variables.get('patron_name')
                        if not second_name:
                            second_name = bot_variables.get('second_name')
                        if not email:
                            email = bot_variables.get('email')
                        if not client_groups:
                            client_groups = bot_variables.get('client_groups')
                        if not living_address:
                            living_address = bot_variables.get('living_address')
                        if not sex:
                            sex = bot_variables.get('sex')
                        if not appointment_confirmation_sms:
                            appointment_confirmation_sms = bot_variables.get('appointment_confirmation_sms')
                        if not lead_source:
                            lead_source = bot_variables.get('lead_source')
                        params_add_client = {'phone': 'phone',
                                           'first_name': 'first_name',
                                           'patron_name': 'patron_name',
                                           'second_name': 'second_name',
                                           'email': 'email',
                                           'client_groups': 'client_groups',
                                           'living_address': 'living_address',
                                           'sex': 'sex',  #1 - male, 0 - female
                                           'appointment_confirmation_sms': 'appointment_confirmation_sms', #1 - yes, 0 - no
                                           'lead_source': 'lead_source'} # where info from
                        status, result = requests.post(api_key, data=params_add_client)
                        # status, result = main_api_request(api_key, 'new_client_Create', params_add_client)  # вызов функции в ней просто запрос к апи (тут можешь просто свой вызов добавить)
                        if status:
                            answer = {'status': '1', 'result': True}
                        else:
                            answer = {'status': '0', 'error': result}
                        client.get_project().increment_send_statistic()
                else:
                    answer = {'status': '0', 'error': "No api_key in 'klientiks_api_key' variable in project settings"}
        except Exception as e:
            answer = {'status': '0', 'error': str(e)}
        return ujson.dumps(answer, ensure_ascii=False)

