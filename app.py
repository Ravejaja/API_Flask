import mysql.connector 
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Byme"   
)

@app.route('/livros', methods=['GET'])
def get_livros():
    my_cursor  = mydb.cursor()
    my_cursor.execute('SELECT * FROM livros')
    meus_livros = my_cursor.fetchall()

    livros = []
    for livro in meus_livros:
        livros.append({
            "id": livro[0],
            "nome": livro[1],
            "autor": livro[2],
            "ano": livro[3],
        })

    return make_response(jsonify({
        "mensagem": "Lista de Livros",
        "dados": livros
    }))

@app.route('/livros/<int:id>', methods=['GET'])
def get_livro_por_id(id):
    my_cursor  = mydb.cursor()
    query = 'SELECT * FROM livros WHERE id = %s'
    my_cursor.execute(query, (id,))
    livro = my_cursor.fetchone()

    if livro:
        livro_dict = {
            "id": livro[0],
            "nome": livro[1],
            "autor": livro[2],
            "ano": livro[3],
        }
        return make_response(jsonify({
            "mensagem": "Livro encontrado",
            "dados": livro_dict
        }))
    else:
        return make_response(jsonify({
            "mensagem": "Livro não encontrado"
        }), 404)


@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro=request.get_json()

    my_cursor  = mydb.cursor()
    query = f"INSERT INTO livros (nome, autor, ano) VALUES ('{novo_livro['nome']}','{novo_livro['autor']}', {novo_livro['ano']})"
    my_cursor.execute(query)
    mydb.commit()

    return make_response(
        jsonify(
            mensagem = 'Livro Adicionado com Sucesso',
            dados = novo_livro
        )
    )


@app.route('/livros/<int:id>', methods=['DELETE'])  
def excluir_livro(id):
    my_cursor  = mydb.cursor()
    query = 'DELETE FROM livros WHERE id = %s'
    my_cursor.execute(query, (id,))
    mydb.commit()

    return make_response(jsonify({
        "mensagem": "Livro Excluido com Sucesso"
    }))

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()

    novo_nome = livro_alterado.get('nome')
    novo_autor = livro_alterado.get('autor')
    novo_ano = livro_alterado.get('ano')

    my_cursor = mydb.cursor()
    query = "UPDATE livros SET nome = %s, autor = %s, ano = %s WHERE id = %s"
    dados_atualizados = (novo_nome, novo_autor, novo_ano, id)

    my_cursor.execute(query, dados_atualizados)
    num_linhas_afetadas = my_cursor.rowcount


    if num_linhas_afetadas > 0:
        # Se pelo menos uma linha foi afetada, significa que o livro foi atualizado com sucesso
        mydb.commit()
        return make_response(jsonify({
            "mensagem": "Livro atualizado com sucesso"
        }))
    else:
        # Se nenhuma linha foi afetada, significa que o livro com o ID especificado não foi encontrado
        return make_response(jsonify({
            "mensagem": "Livro não encontrado ou nenhum dado foi alterado"
        }), 404)

    # Retornar a resposta JSON
    return make_response(jsonify({
        "mensagem": "Livro atualizado com sucesso"
    }))

@app.route('/register', methods=['POST'])
def register():
    new_user=request.get_json()
    my_cursor=mydb.cursor()

    query = f"INSERT INTO users(email, pass) VALUES ('{new_user['email']}', {new_user['password']})"
    my_cursor.execute(query)
    mydb.commit()

    return make_response(
        jsonify(
            msg = 'User created successfully',
            succes = True,
            data = new_user
        ),
        201
    )

app.run(port=5000,host='localhost',debug=True)