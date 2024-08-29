from cidades import Cidades
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 10
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 15
        self.container6.pack()

        self.titulo = Label(self.container1,text ="Informe os dados da cidade(nome/uf):")
        self.titulo["font"] = ("Arial Black","14","bold")
        self.titulo.pack()
        self.lblidcidade= Label(self.container2,
        text ="idcidade:",font=self.fonte, width = 10)
        self.lblidcidade.pack(side=LEFT)
        self.txtidcidade = Entry(self.container2)
        self.txtidcidade["width"] = 10
        self.txtidcidade["font"] = self.fonte
        self.txtidcidade.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar",font= self.fonte,width=10)
        self.btnBuscar["command"] = self.buscarcid
        self.btnBuscar.pack(side=RIGHT)
        self.lblnomecid = Label(self.container3, text="Cidade:",
        font=self.fonte, width=10)
        self.lblnomecid.pack(side=LEFT)
        self.txtnomecid = Entry(self.container3)
        self.txtnomecid["width"] = 25
        self.txtnomecid["font"] = self.fonte
        self.txtnomecid.pack(side=LEFT)
        self.lbluf = Label(self.container4, text="UF:",
        font=self.fonte, width=10)
        self.lbluf.pack(side=LEFT)
        self.txtuf = Entry(self.container4)
        self.txtuf["width"] = 25
        self.txtuf["font"] = self.fonte
        self.txtuf.pack(side=LEFT)

        self.bntInsert = Button(self.container5, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserircid
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container5, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.atualcid
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container5, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.deletecid
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container6, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserircid(self):
            user = Cidades()
            user.nomecid = self.txtnomecid.get()
            user.uf = self.txtuf.get()
            self.lblmsg["text"] = user.insertcid()
            self.txtnomecid.delete(0, END)
            self.txtuf.delete(0, END)

    def atualcid(self):
         user = Cidades()
         user.idcidade = self.txtidcidade.get()
         user.nomecid = self.txtnomecid.get()
         user.uf = self.txtuf.get()
         self.lblmsg["text"] = user.updatecid()
         self.txtidcidade.delete(0, END)
         self.txtnomecid.delete(0, END)
         self.txtuf.delete(0, END)

    def deletecid(self):
        user = Cidades()
        user.idcidade = self.txtidcidade.get()
        self.lblmsg["text"] = user.deletecid()
        self.txtidcidade.delete(0, END)
        self.txtnomecid.delete(0, END)
        self.txtuf.delete(0, END)

    def buscarcid(self):
         user = Cidades()
         idcidade = self.txtidcidade.get()
         self.lblmsg["text"] = user.selectcid(idcidade)
         self.txtidcidade.delete(0, END)
         self.txtidcidade.insert(INSERT, user.idcidade)
         self.txtnomecid.delete(0, END)
         self.txtnomecid.insert(INSERT, user.nomecid)
         self.txtuf.delete(0, END)
         self.txtuf.insert(INSERT,user.uf)


root = Tk()
Application(root)
root.mainloop()