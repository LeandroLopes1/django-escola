import requests

headers = {'Authorization': 'Token 4179a1980713bdec37394229bca2901048d2871b'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v1/avaliacoes/'

curso_atualizado = {
    'titulo': 'Novo curso de Scrum3',
    'url': 'https://www.geekuniversity.com/course/scrum3/',
}

# Buscando o curso com ID 6 para atualizar
# curso = requests.get (url_base_cursos + '6/', headers=headers)
# print(curso.json())

resultado = requests.put(url_base_cursos + '6/', headers=headers, data=curso_atualizado)

# Testando o codigo de status HHTP 

assert resultado.status_code == 200

# Testando se o titulo do curso retornado é o mesmo que o enviado

assert resultado.json()['titulo'] == curso_atualizado['titulo']