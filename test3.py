import requests

# Правильный запрос
job = {
    'team_leader': 1,
    'job': 'ingeneer',
    'collaborators': '2 3',
    'work_size': 10,
    'is_finished': True
}

t1 = requests.post('http://127.0.0.1:8080/api/jobs', json=job).json()
print(t1)
#Запрос с не всеми полями
job = {
    'team_leader': 1,
    'job': 'ingeneer',
    'work_size': '10',
    'is_finished': True
}

t2 = requests.post('http://127.0.0.1:8080/api/jobs', json=job).json()
print(t2)
#Запрос с пустым объектом
job = {
}

t3 = requests.post('http://127.0.0.1:8080/api/jobs', json=job).json()
print(t3)
#Запрос с неправильными полями
job = {
    'team_leader': "capitan",
    'job': 'ingeneer',
    'collaborators': '2 3',
    'work_size': '10',
    'is_finished': True
}

t4 = requests.post('http://127.0.0.1:8080/api/jobs', json=job).json()
print(t4)
