import requests

account_id = "c6637265cdbe"
user_id ="c35a9cedb0ce"
access_token = "730ba9573dfb6d3930ec8deefcbf8ff8"

#задание a - получение списка сотрудников
# url_empl_list = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}/t/{access_token}/m/Users/")
# list_of_employees = requests.get(url_empl_list)
# print(list_of_employees.json())

def list_of_employees(client):
    try:
        account_id = client.get_var_val('klientiks_account_id')
        user_id = client.get_var_val('klientiks_user_id')
        access_token = client.get_var_val('klientiks_access_token')
        if account_id and user_id and access_token:
            url_empl_list = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}"
                             f"/t/{access_token}/m/Users/")
            response = requests.get(url_empl_list)
            if response.ok:
                data_list_of_employees = response.json()
                if data_list_of_employees.get('items'):
                    if data_list_of_employees.get('items') == 'No data':
                        answer = {'status': '1', 'result': 'No data'}
                    else:
                        answer = {'status': '1', 'result': data_list_of_employees.get('items')}
                else:
                    answer = {'status': '0', 'error': response.json()}
                client.get_project().increment_send_statistic()
            else:
                answer = {'status': '0', 'error': response.json()}
        else:
            answer = {'status': '0', 'error': "No account_id/user_id/access_token in 'klientiks_api_key'"
                                              " variable in project settings"}
    except Exception as e:
        answer = {'status': '0', 'error': str(e)}
    return ujson.dumps(answer, ensure_ascii=False)

#задание b - получить доступное время для записи
# params_free_date = {'start_day': '2022-03-07', 'finish_day': '2022-03-07', 'service_id[]': '1210056',
#         'executor_id': '120933'}
# url_free_date = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}/t/{access_token}/m/availableTimes")
# data_free_date = requests.get(url_free_date, params=params_free_date)
# print(data_free_date.json())

def get_free_date(client,start_day,finish_day=None,service_id=None,executor_id=None):
    try:
        account_id = client.get_var_val('klientiks_account_id')
        user_id = client.get_var_val('klientiks_user_id')
        access_token = client.get_var_val('klientiks_access_token')
        if account_id and user_id and access_token:
            if not start_day:
                    return ujson.dumps({'status': '0', 'error': 'Missing required variables - start_day'},
                                           ensure_ascii=False)
            params_free_date = {'start_day': start_day,
                                'finish_day': finish_day,
                                'service_id[]': service_id,
                                'executor_id': executor_id}
            url_free_date = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}"
                             f"/t/{access_token}/m/availableTimes")
            response = requests.get(url_free_date, params=params_free_date)
            if response.ok:
                data_get_free_date = response.json()
                if data_get_free_date.get('items'):
                    if data_get_free_date.get('items') == 'No data':
                        answer = {'status': '1', 'result': 'No data'}
                    else:
                        answer = {'status': '1', 'result': data_get_free_date.get('items')}
                else:
                    answer = {'status': '0', 'error': response.json()}
                client.get_project().increment_send_statistic()
            else:
                answer = {'status': '0', 'error': response.json()}
        else:
            answer = {'status': '0', 'error': "No account_id/user_id/access_token in 'klientiks_api_key'"
                                              " variable in project settings"}
    except Exception as e:
     answer = {'status': '0', 'error': str(e)}
    return ujson.dumps(answer, ensure_ascii=False)

#задание с - добавить визит для основного клиента
# url_add_record = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}/t/{access_token}/m/Appointments/s/apiAdd/")
# params_add_record = {'executor_id': 120933, 'service_id[]': 1210056, 'start_datetime': '2022-03-07 11:00:00', 'first_name': 'Николай', 'phone': '79111100005','subclient_name': 'Гарри','appointment_id': 11111,'living_address': 'Невский 1','birth_date': '23.02.1991'}
# resp = requests.post(url_add_record, data=params_add_record)
# print(requests.get(url_add_record, params=params_add_record))
# print(resp.json())

def add_record(client,bot_variables,name,phone,executor_id,service_id,start_datetime,
                appointment_id=None,living_address=None,birth_date=None,subclient_name=None):
     try:
            account_id = client.get_var_val('klientiks_account_id')
            user_id = client.get_var_val('klientiks_user_id')
            access_token = client.get_var_val('klientiks_access_token')
            if account_id and user_id and access_token:
                if not name:
                    name = bot_variables.get('name')
                    if not name:
                        return ujson.dumps({'status': '0', 'error': 'Missing required variables - name'},
                                           ensure_ascii=False)
                if not phone:
                    phone = bot_variables.get('phone')
                    if not phone:
                        return ujson.dumps({'status': '0', 'error': 'Missing required variables - phone'},
                                           ensure_ascii=False)
                if not executor_id:
                    return ujson.dumps({'status': '0', 'error': 'Missing required variables - executor_id'},
                                       ensure_ascii=False)
                if not service_id:
                    return ujson.dumps({'status': '0', 'error': 'Missing required variables - service_id'},
                                       ensure_ascii=False)
                if not start_datetime:
                    return ujson.dumps({'status': '0', 'error': 'Missing required variables - start_datetime'},
                                       ensure_ascii=False)
                params_add_record = {'first_name': name,
                                     'phone': phone,
                                     'executor_id': executor_id,
                                     'service_id[]': service_id,
                                     'start_datetime': start_datetime,
                                     'appointment_id': appointment_id,
                                     'living_address': living_address,
                                     'birth_date': birth_date,
                                     'subclient_name': subclient_name}
                url_add_record = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}"
                                f"/t/{access_token}/m/Appointments/s/apiAdd/")
                response = requests.post(url_add_record, data=params_add_record)
                if response.ok:
                    data_add_record = response.json()
                    if data_add_record.get('object'):
                        if data_add_record.get('object') == 'No data':
                            answer = {'status': '1', 'result': 'No data'}
                        else:
                            answer = {'status': '1', 'result': data_add_record.get('object')}
                    else:
                        answer = {'status': '0', 'error': response.json()}
                    client.get_project().increment_send_statistic()
                else:
                    answer = {'status': '0', 'error': response.json()}
            else:
                answer = {'status': '0', 'error': "No account_id/user_id/access_token in 'klientiks_api_key'"
                                                  " variable in project settings"}
     except Exception as e:
            answer = {'status': '0', 'error': str(e)}
     return ujson.dumps(answer, ensure_ascii=False)


# Задание d - добавить клиента
# url_add_сlient = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}/t/{access_token}/m/Clients/")
# params_add_client = {'phone': '74445550011', 'first_name': 'Иван', 'patron_name': 'Иванович', 'second_name': 'Иванов',
#                      'email': 'test@test.com', 'client_groups': 'Новенький', 'living_address': 'Невский проспект, 25',
#                      'sex': '1', 'appointment_confirmation_sms': '1', 'lead_source': 'бот'}
# resp_client = requests.post(url_add_сlient, data=params_add_client)
# print(requests.get(url_add_сlient, params=params_add_client))
# print(resp_client.json())

def add_new_clients(client,bot_variables,phone,name,patron_name=None,second_name=None,email=None,living_address=None,
                    sex=None,appointment_confirmation_sms=None,lead_source=None,client_groups=None):
        try:
                account_id = client.get_var_val('klientiks_account_id')
                user_id = client.get_var_val('klientiks_user_id')
                access_token = client.get_var_val('klientiks_access_token')
                if account_id and user_id and access_token:
                        if not phone:
                              phone = bot_variables.get('phone')
                              if not phone:
                                  return ujson.dumps({'status': '0', 'error': 'Missing required variables - phone'},
                                                     ensure_ascii=False)
                        if not name:
                            first_name = bot_variables.get('name')
                            if not name:
                                return ujson.dumps({'status': '0', 'error': 'Missing required variables - name'},
                                                     ensure_ascii=False)
                        if not email:
                            email = bot_variables.get('email')
                        params_add_client = {'phone': phone,
                                           'first_name': name,
                                           'patron_name': patron_name,
                                           'second_name': second_name,
                                           'email': email,
                                           'living_address': living_address,
                                           'sex': sex,  #1 - male, 0 - female
                                           'appointment_confirmation_sms': appointment_confirmation_sms, #1 - yes, 0 - no
                                           'lead_source': lead_source,
                                           'client_groups': client_groups} # where info from
                        url_add_сlient = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}"
                                          f"/t/{access_token}/m/Clients/")
                        response = requests.post(url_add_сlient, data=params_add_client)
                        if response.ok:
                            data_add_new_klient=response.json()
                            if data_add_new_klient.get('object'):
                                    if data_add_new_klient.get('object')== 'No data':
                                        answer = {'status': '1', 'result': 'No data'}
                                    else:
                                        answer = {'status': '1', 'result': data_add_new_klient.get('object')}
                            else:
                                    answer = {'status': '0', 'error': response.json()}
                            client.get_project().increment_send_statistic()
                        else:
                            answer = {'status': '0', 'error': response.json()}
                else:
                    answer = {'status': '0', 'error': "No account_id/user_id/access_token in 'klientiks_api_key'"
                                                      " variable in project settings"}
        except Exception as e:
            answer = {'status': '0', 'error': str(e)}
        return ujson.dumps(answer, ensure_ascii=False)
