import requests

# GET Acaliacoes

# avaliacoes = requests.get('http://localhost:8000/api/v1/avaliacoes/')

# Acessando o codigo de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta 
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros 
# print(avaliacoes.json()['count'])

# Acessando a proxima pagina de resultados
#print(avaliacoes.json()['next'])

# Acessando os resultados desta pagina
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando somente a nome da pessoa que fez a ultima avaliacao
# print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliacao

#avaliacao = requests.get('http://localhost:8000/api/v1/avaliacoes/7/')

# print(avaliacao.json())

# GET Cursos

headers = { 'Authorization': 'Token 4179a1980713bdec37394229bca2901048d2871b' }

cursos = requests.get(url='http://localhost:8000/api/v1/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())