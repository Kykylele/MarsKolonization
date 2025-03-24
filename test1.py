import requests

t1 = requests.get('http://127.0.0.1:8080/api/jobs').json()
t2 = requests.get('http://127.0.0.1:8080/api/jobs/1').json()
t3 = requests.get('http://127.0.0.1:8080/api/jobs/0').json()
t4 = requests.get('http://127.0.0.1:8080/api/jobs/aaa').json()
print(t1)
print(t2)
print(t3)
print(t4)
