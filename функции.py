import requests
klientiks= {'account_id':["c6637265cdbe","26ab3bd1fd11"],'user_id':["c35a9cedb0ce","47e8ec252a42"],
            'access_token':["730ba9573dfb6d3930ec8deefcbf8ff8","e2eaa726b1602312c0d17eedeb54bb3f"]}

def url_for_operation(request,client,api_vars):
    # выберете запрос: 'list_of_employees' - получить cписок сотрудников,'free_date' - получить свободное время,
    # 'add_record' - добавить запись, 'add_сlient' - добавить клиента
    ## client [0] - мой, [1] - пример
    operation_urls = {
        'list_of_employees': f"https://klientiks.ru/clientix/Restapi/add/a/{(api_vars.get('account_id'))[client]}"
                             f"/u/{(api_vars.get('user_id'))[client]}"
                             f"/t/{(api_vars.get('access_token'))[client]}/m/Users/",
        'free_date': f"https://klientiks.ru/clientix/Restapi/list/a/{(api_vars.get('account_id'))[client]}"
                     f"/u/{(api_vars.get('user_id'))[client]}/t/"
                     f"{(api_vars.get('access_token'))[client]}/m/availableTimes",
        'add_record': f"https://klientiks.ru/clientix/Restapi/add/a/{(api_vars.get('account_id'))[client]}"
                      f"/u/{(api_vars.get('user_id'))[client]}"
                      f"/t/{(api_vars.get('access_token'))[client]}/m/Appointments/s/apiAdd/",
        'add_сlient': f"https://klientiks.ru/clientix/Restapi/add/a/{(api_vars.get('account_id'))[client]}"
                      f"/u/{(api_vars.get('user_id'))[client]}"
                      f"/t/{(api_vars.get('access_token'))[client]}/m/Clients/"}
    return operation_urls.get(request)

def list_of_employees(client,api_vars):
      #получить список сотрудников
      url_list_of_employees = url_for_operation('list_of_employees',client,api_vars)
      get_list_of_employees = requests.get(url_list_of_employees)
      return get_list_of_employees.json()

def free_date(client,api_vars,start_day,finish_day=None,service_id=None,executor_id=None):
        # получить список сотрудников
        url_free_date = url_for_operation('free_date',client,api_vars)
        params_free_date = {'start_day': start_day,
                            'finish_day': finish_day,
                            'service_id[]': service_id,
                            'executor_id': executor_id}
        get_free_date = requests.get(url_free_date, params=params_free_date)
        return get_free_date.json()

def add_record(client,api_vars,executor_id,service_id,start_datetime,first_name,phone,subclient_name=None,
                appointment_id=None,living_address=None,birth_date=None):
            #добавить запись
            url_add_record = url_for_operation('add_record',client,api_vars)
            params_add_record = {'executor_id': executor_id,
                                'service_id[]': service_id,
                                'start_datetime': start_datetime,
                                'first_name': first_name,
                                'phone': phone,
                                'subclient_name': subclient_name,
                                'appointment_id': appointment_id,
                                'living_address': living_address,
                                'birth_date': birth_date}
            post_add_record = requests.post(url_add_record, data=params_add_record)
            get_add_record = requests.get(url_add_record, params=params_add_record)
            if get_add_record:
                return post_add_record.json()
            else:
                print ('Failed')

def add_new_clients(client,api_vars,phone,first_name,patron_name=None,second_name=None,email=None,living_address=None,
                    sex=None,appointment_confirmation_sms=None,lead_source=None,client_groups=None):
    #добавить нового клиента
    url_add_client = url_for_operation('add_сlient', client, api_vars)
    params_add_client = {'phone': phone,
                         'first_name': first_name,
                         'patron_name': patron_name,
                         'second_name': second_name,
                         'email': email,
                         'client_groups': client_groups,
                         'living_address': living_address,
                         'sex': sex,  # 1 - male, 0 - female
                         'appointment_confirmation_sms': appointment_confirmation_sms,  # 1 - yes, 0 - no
                         'lead_source': lead_source}  # where info from
    post_add_client = requests.post(url_add_client, data=params_add_client)
    get_add_client = requests.get(url_add_client, data=params_add_client)
    if get_add_client:
        return post_add_client.json()
    else:
        print('Failed')