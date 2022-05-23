import requests

class TestCursos:
    headers = {'Authorization': 'Token 5670074ed34ebca21f0641afa3f05a1ef7b2778f'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v1/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso_id(self):
        curso = requests.get(self.url_base_cursos + '3/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        curso = {
            'titulo': 'Curso de Programação com Ruby on Rails 345',
            'url': 'https://www.udemy.com/course/programacao-com-ruby-on-rails345/',
        }

        resultado = requests.post(self.url_base_cursos, headers=self.headers, data=curso)

        assert resultado.status_code == 201
        assert resultado.json()['titulo'] == curso['titulo']

    def test_put_curso(self):
        curso = {
            'titulo': 'Novo curso de Ruby on Rails 3',
            'url': 'https://www.udemy.com/course/programacao-com-ruby-on-rails/novo3/',
        }

        resultado = requests.put(self.url_base_cursos + '2/', headers=self.headers, data=curso)

        assert resultado.status_code == 200
       
    def test_put_titulo_curso(self):
        curso = {
            'titulo': 'Novo curso de Ruby on Rails 22',
            'url': 'https://www.udemy.com/course/programacao-com-ruby-on-rails/novo22/',
        }

        resultado = requests.put(self.url_base_cursos + '2/', headers=self.headers, data=curso)

        assert resultado.status_code == 200
        assert resultado.json()['titulo'] == curso['titulo']

    def test_delete_curso(self):
        resultado = requests.delete(self.url_base_cursos + '2/', headers=self.headers)

        assert resultado.status_code == 204
        assert len(resultado.content) == 0