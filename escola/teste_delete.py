import requests

headers = {'Authorization': 'Token 5670074ed34ebca21f0641afa3f05a1ef7b2778f'}

url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v1/avaliacoes/'

resultado = requests.delete(url_base_cursos + '6/', headers=headers)

# Testando o codigo de status HHTP

assert resultado.status_code == 204

# Testando se o tamanho do conteudo é 0

assert len(resultado.content) == 0