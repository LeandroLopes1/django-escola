import requests

headers = {'Authorization': 'Token 4179a1980713bdec37394229bca2901048d2871b'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v1/avaliacoes/'

novo_curso = {
    'titulo': 'Gerencia Agil de projeto com Scrum 2',
    'url': 'https://www.udemy.com/course/gerencia-agil-de-projeto-com-scrum2/',
}

resultado = requests.post(url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status HHTP 201

assert resultado.status_code == 201

# Testando se o titulo do curso retornado é o mesmo que o enviado

assert resultado.json()['titulo'] == novo_curso['titulo']