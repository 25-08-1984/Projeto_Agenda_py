from banco import Banco
from tkinter import messagebox


class Clientes(object):
    def __init__(self,idcliente = 0, nomecli= "",  enderecocli = "",cpfcli ="",telefonecli = "",emailcli=""):
        self.info={}
        self.idcliente = idcliente
        self.nomecli = nomecli
        self.enderecocli     = enderecocli
        self.cpfcli = cpfcli
        self.telefonecli = telefonecli
        self.emailcli =emailcli

    def insertcli(self):
        banco = Banco()
        try:
            c= banco.conexao.cursor()
            c.execute("insert into tbl_clientes(nomecli,enderecocli,cpfcli,telefonecli,emailcli) values('" + self.nomecli + "',"
                        " '" + self.enderecocli + "', '" + self.cpfcli + "', '" + self.telefonecli + "','" + self.emailcli + "')")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo('','Cliente cadastrado(a) com sucesso!')
        except:
            messagebox.showinfo('','Ocorreu um erro no cadastro!')

    def updatecli(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_clientes set nomecli = '" + self.nomecli + "',enderecocli= '" + self.enderecocli + "',cpfcli = '" + self.cpfcli + "',telefonecli= '" + self.telefonecli + "',emailcli= '" + self.emailcli + "'   where idcliente = " + self.idcidade +  "")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo('','Cliente alterado/a com sucesso!')
        except:
            messagebox.showinfo('','Ocorreu um erro na alteração da clientes!')
    def deletecli(self):
        banco = Banco()
        try:
            c = banco.conexão.cursor()
            c.execute("delete from tbl_clientes where idcliente =  " +  self.idcliente  + " ")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("",'Registro apagado com sucesso!')
        except:
            messagebox.showinfo("",'Ocorreu um erro na exclusão!')

    def selectcli(self,idcliente):
        banco = Banco()
        try :
            c = banco.conexao.cursor()
            c.execute("select  * from tbl_clientes where idcliente = " + idcliente + "  ")
            for linha in c:
                self.idcliente = linha[0]
                self.nomecli = linha[1]
                self.enderecocli = linha[2]
                self.cpfcli = linha[3]
                self.telefonecli = linha[4]
                self.emailcli = linha[5]

                c.close()
                messagebox.showinfo("","Busca feita com sucesso!")

        except:
                messagebox.showinfo("","Ocorreu um erro na busca do usuário")
