!pip install flask

from flask import Flask,jsonify, request

app = Flask(__name__)
postagens = [
    {
        'titulo': 'Minha História',
        'autor': 'Amanda Dias'
    },
    {
        'titulo': 'Novo dispositivo',
        'autor': 'Howard Stringer'
     }
    ]

# Rota padrão - GET http://localhost:5000

@app.route('/')
def obter_postagens():
    return jsonify(postagens)

app.run(port=5000, host='localhost', debug=True)


'''
1 - Definir o objetivo da API:
    ex: Iremos montar uma api de blog, onde podera consultar, editar, criar e excluir postagens em um blog usando API
2 - Qual sera o URL base do API?
    ex: Quando é criado uma  aplicação local ela terá um url do tipo http://localhost:5000 , porem quando for subir para nuvem, terá que comprar ou usar um domínio como url base, IMAGINE devaprender.com/api
3 - Quais os endpoints?
    ex: Se o requisito é de poder consultar, editar, criar e excluir, terá que disponibilizar os endpoints para essas questões
        >/postagens
4 - Quais recursos será disponibilizado pelo api?
    ex: informações sobre as postagens
5 - Quais verbos http serão disponibilizados?
    ex: GET - POST - PUT - DELETE
6 - Quais são os URL completos para cada um?
    ex: http://localhost:5000
            GET - http://localhost:5000/postagens - para obter todos recursos
            GET id - http://localhost:5000/postagens/1 - para obter recurso especifico
            POST - http://localhost:5000/postagens - para criar novo recurso
            PUT - http://localhost:5000/postagens - para alterar um recurso
            DELETE - http://localhost:5000/postagens - para deletar um recurso
        Essa lista é importante pois podera ser passada para uma documentação para que pessoas saibam quais recursos tem disponiveis para acesso
'''
