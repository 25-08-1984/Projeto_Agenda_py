import sqlite3

class Banco():
    def __init__(self):
        self.conexão = None
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_usuarios(
        idusuario integer primary key autoincrement,
        nome text,
        telefone text,
        email text,
        usuario text,
        senha text)""")

        c =self.conexao.cursor()
        c.execute("""create table if not exists tbl_cidades(
        idcidade integer primary key autoincrement,
        nomecid text,
        uf       text)""")

        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_clientes(
               idcliente integer primary key autoincrement,
               nomecli text,
               enderecocli text,
               cpfcli  text,
               telefonecli text,
               emailcli text
               
               
               
               )""")




        self.conexao.commit()
        c.close()