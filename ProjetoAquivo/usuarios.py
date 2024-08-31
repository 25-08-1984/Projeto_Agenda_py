from banco import Banco
from tkinter import messagebox
class Usuarios(object):
    def __init__(self, idusuario = 0, nome = "", telefone = "",
        email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tbl_usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" +
            self.telefone + "', '" + self.email + "', '" +
            self.usuario + "', '" + self.senha + "' )")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso","Cidade inserida com sucesso!")
        except:
            messagebox.showinfo("Erro","Ocorreu um erro na inserção do usuário")
    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_usuarios set nome = '" + self.nome + "',telefone = '" + self.telefone + "', email = '" + self.email +
            "', usuario = '" + self.usuario + "', senha = '" + self.senha +
            "' where idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso","Usuário atualizado com sucesso!")
        except:
            messagebox.showinfo("","Usuário atualizado com sucesso!")
    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from tbl_usuarios where idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("","Usuário excluído com sucesso!")
        except:
            messagebox.showinfo("","Ocorreu um erro na exclusão do usuário")

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from tbl_usuarios where idusuario = " + idusuario + " ")
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            c.close()
            messagebox.showinfo("","Busca feita com sucesso!")
        except:
            messagebox.showinfo("","Ocorreu um erro na busca do usuário")

