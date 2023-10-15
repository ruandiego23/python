import sqlite3


def manipulaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()


def selecionaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)


def ManipulacaonDados():
    comandoInsert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado Teste', 'XX', 'Teste Inclusão')"
    pathDB = "C:\\Users\\ruand\\PycharmProjects\\Meus_exercicios\\link\\db.sqlite3"
    comandoSelect = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"

    manipulaDados(pathDB, comandoInsert)
    selecionaDados(pathDB, comandoSelect)

ManipulacaonDados()