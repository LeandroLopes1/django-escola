import requests

headers = {'Authorization': 'Token 4179a1980713bdec37394229bca2901048d2871b'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v1/avaliacoes/'

resultado = requests.get(url_base_cursos, headers=headers)

#  print(resultado.json())

# Testando se o endpoint está correto

assert resultado.status_code == 200

# Testando a quantidade de registros

assert resultado.json()['count'] == 5

# Testando de o Titulo do primeiro curso está correto

assert resultado.json()['results'][0]['titulo'] == 'Programação para Web com Django Framework'