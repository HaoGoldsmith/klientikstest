import requests
#добавить клиента
account_id = "c6637265cdbe"
user_id ="c35a9cedb0ce"
access_token = "730ba9573dfb6d3930ec8deefcbf8ff8"
url_add_сlient = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}/t/{access_token}/m/Clients/")
params_add_client = {'phone': '74445550011', 'first_name': 'Иван', 'patron_name': 'Иванович', 'second_name': 'Иванов',
                     'email': 'test@test.com', 'client_groups': 'Новенький', 'living_address': 'Невский проспект, 25',
                     'sex': '1', 'appointment_confirmation_sms': '1', 'lead_source': 'бот'}
resp_client = requests.post(url_add_сlient, data=params_add_client)
print(resp_client.json())

#функция
def add_new_clients(client,bot_variables,phone,first_name,patron_name=None,second_name=None,email=None,living_address=None,
                    sex=None,appointment_confirmation_sms=None,lead_source=None,client_groups=None):
#добавить клиента
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
