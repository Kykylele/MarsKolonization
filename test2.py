import requests

t1 = requests.get('http://127.0.0.1:8080/api/v2/users/1').json() # правильный гет запрос
t2 = requests.get('http://127.0.0.1:8080/api/v2/users/-1').json() # неправильный гет запрос
t3 = requests.delete('http://127.0.0.1:8080/api/v2/users/1').json() # правильный делете запрос
t4 = requests.delete('http://127.0.0.1:8080/api/v2/users/-1').json() # неправильный делете запрос
# далее запросы ко всем пользователям
t5 = requests.get('http://127.0.0.1:8080/api/v2/users').json() # гет запрос
t6 = requests.post('http://127.0.0.1:8080/api/v2/users').json() # пост запрос
t7 = {
'surname': 'Fric',
'name': 'Tyty',
'age': 7000000000000,
'position': 'captain',
'speciality': 'engeneer',
'address': '1',
'email': 'tyty@email.com',
'hashed_password': '787878'
} # правильный пост запрос
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
