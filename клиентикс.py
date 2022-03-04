import requests
# получение списка сотрудников
account_id = "c6637265cdbe"
user_id ="c35a9cedb0ce"
access_token = "730ba9573dfb6d3930ec8deefcbf8ff8"
url_klientiks = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}/t/{access_token}/m/Users/")
list_of_employees = requests.get(url_klientiks)
list_of_employees.encoding = 'utf-8'
print(list_of_employees.json())

#получить доступное время для записи
params_free_date = {'start_day': '2022-03-07', 'finish_day': '2022-03-07', 'service_id[]': '1210056',
        'executor_id': '120923'}
url_free_date = (f"https://klientiks.ru/clientix/Restapi/list/a/{account_id}/u/{user_id}/t/{access_token}/m/availableTimes")
data_free_date = requests.get(url_free_date, params=params_free_date)
data_free_date.encoding = 'utf-8'
print(data_free_date.json())

#добавить визит для основного клиента
url_add_record = (f"https://klientiks.ru/clientix/Restapi/add/a/{account_id}/u/{user_id}/t/{access_token}/m/Appointments/s/apiAdd/")
params_add_record = {'executor_id': 120933, 'service_id[]': 1210056, 'start_datetime': '2022-03-07 11:00:00', 'first_name': 'Николай', 'phone': '79111100005','subclient_name': 'Гарри','appointment_id': 11111,'living_address': 'Невский 1','birth_date': '23.02.1991'}
resp = requests.post(url_add_record, data=params_add_record)
resp.encoding = 'utf-8'
print(resp.json())
