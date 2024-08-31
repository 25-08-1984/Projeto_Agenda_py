from cliente import Clientes
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
         self.container4["pady"] = 5
         self.container4.pack()
         self.container5 = Frame(master)
         self.container5["padx"] = 20
         self.container5["pady"] = 5
         self.container5.pack()
         self.container6 = Frame(master)
         self.container6["padx"] = 20
         self.container6["pady"] = 5
         self.container6.pack()
         self.container7 = Frame(master)
         self.container7["padx"] = 20
         self.container7["pady"] = 5
         self.container7.pack()
         self.container8 = Frame(master)
         self.container8["padx"] = 20
         self.container8["pady"] = 10
         self.container8.pack()
         self.container9 = Frame(master)
         self.container9["pady"] = 15
         self.container9.pack()

         self.titulo = Label(self.container1, text="Informe os dados :")
         self.titulo["font"] = ("Calibri", "9", "bold")
         self.titulo.pack()
         self.lblidcliente = Label(self.container2,text="idcliente:", font=self.fonte, width=10)
         self.lblidcliente.pack(side=LEFT)

         self.txtidcliente = Entry(self.container2)
         self.txtidcliente["width"] = 10
         self.txtidcliente["font"] = self.fonte
         self.txtidcliente.pack(side=LEFT)
         self.btnBuscar = Button(self.container2, text="Buscar",
                                 font=self.fonte, width=10)
         self.btnBuscar["command"] = self.buscarcliente
         self.btnBuscar.pack(side=RIGHT)

         self.lblnomecli = Label(self.container3, text="Nome:",
                              font=self.fonte, width=10)
         self.lblnomecli.pack(side=LEFT)
         self.txtnomecli = Entry(self.container3)
         self.txtnomecli["width"] = 25
         self.txtnomecli["font"] = self.fonte
         self.txtnomecli.pack(side=LEFT)

         self.lblenderecocli = Label(self.container4, text="Endereço:",
                                  font=self.fonte, width=10)
         self.lblenderecocli.pack(side=LEFT)
         self.txtenderecocli = Entry(self.container4)
         self.txtenderecocli["width"] = 25
         self.txtenderecocli["font"] = self.fonte
         self.txtenderecocli.pack(side=LEFT)

         self.lblcpfcli = Label(self.container5, text= "CPF:",
                               font=self.fonte, width=10)
         self.lblcpfcli .pack(side=LEFT)
         self.txtcpfcli = Entry(self.container5)
         self.txtcpfcli ["width"] = 25
         self.txtcpfcli ["font"] = self.fonte
         self.txtcpfcli .pack(side=LEFT)

         self.lbltelefonecli = Label(self.container6, text="Telefone:",
                                 font=self.fonte, width=10)
         self.lbltelefonecli.pack(side=LEFT)
         self.txttelefonecli = Entry(self.container6)
         self.txttelefonecli["width"] = 25
         self.txttelefonecli["font"] = self.fonte
         self.txttelefonecli.pack(side=LEFT)

         self.lblemailcli = Label(self.container7, text="Email:",
                               font=self.fonte, width=10)
         self.lblemailcli.pack(side=LEFT)
         self.txtemailcli = Entry(self.container7)
         self.txtemailcli["width"] = 25
         self.txtemailcli["font"] = self.fonte
         self.txtemailcli.pack(side=LEFT)

         self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
         self.bntInsert["command"] = self.inserircliente
         self.bntInsert.pack(side=LEFT)

         self.bntAlterar = Button(self.container8, text="Alterar",
                                  font=self.fonte, width=12)
         self.bntAlterar["command"] = self.alterarcliente
         self.bntAlterar.pack(side=LEFT)

         self.bntExcluir = Button(self.container8, text="Excluir",
                                  font=self.fonte, width=12)
         self.bntExcluir["command"] = self.excluircliente
         self.bntExcluir.pack(side=LEFT)

         self.lblmsg = Label(self.container9, text="")
         self.lblmsg["font"] = ("Verdana", "9", "italic")
         self.lblmsg.pack()

    def inserircliente(self):
         user = Clientes()
         user.nomecli = self.txtnomecli.get()
         user.enderecocli = self.txtenderecocli.get()
         user.cpfcli = self.txtcpfcli.get()
         user.telefonecli = self.txttelefonecli.get()
         user.emailcli = self.txtemailcli.get()
         self.lblmsg["text"] = user.insertcli()
         self.txtidcliente.delete(0, END)
         self.txtnomecli.delete(0, END)
         self.txtenderecocli.delete(0, END)
         self.txtcpfcli.delete(0, END)
         self.txttelefonecli.delete(0, END)
         self.txtemailcli.delete(0, END)


    def alterarcliente(self):
        user = Clientes()
        user.idcliente = self.txtidcliente.get()
        user.nomecli = self.txtnomecli.get()
        user.enderecocli = self.txtenderecocli.get()
        user.cpfcli = self.txtcpfcli.get()
        user.telefonecli = self.txttelefonecli.get()
        user.emailcli = self.txtemailcli.get()
        self.lblmsg["text"] = user.updatecli()
        self.txtidcliente.delete(0, END)
        self.txtnomecli.delete(0, END)
        self.txtenderecocli.delete(0, END)
        self.txtcpfcli.delete(0, END)
        self.txttelefonecli.delete(0, END)
        self.txtemailcli.delete(0, END)


    def excluircliente(self):
        user = Clientes()
        user.idcliente = self.txtidcliente.get()
        self.lblmsg["text"] = user.deletecli()
        self.txtidcliente.delete(0, END)
        self.txtnomecli.delete(0, END)
        self.txtenderecocli.delete(0, END)
        self.txtcpfcli.delete(0, END)
        self.txttelefonecli.delete(0, END)
        self.txtemailcli.delete(0, END)


    def buscarcliente(self):
        user = Clientes()
        idcliente = self.txtidcliente.get()
        self.lblmsg["text"] = user.selectcli(idcliente)
        self.txtidcliente.delete(0, END)
        self.txtidcliente.insert(INSERT, user.idcliente)
        self.txtnomecli.delete(0, END)
        self.txtnomecli.insert(INSERT, user.nomecli)
        self.txtenderecocli.delete(0, END)
        self.txtenderecocli.insert(INSERT, user.enderecocli)
        self.txtcpfcli.delete(0, END)
        self.txtcpfcli.insert(INSERT, user.cpfcli)
        self.txttelefonecli.delete(0, END)
        self.txttelefonecli.insert(INSERT, user.telefonecli)
        self.txtemailcli.delete(0, END)
        self.txtemailcli.insert(INSERT, user.emailcli)


root = Tk()
Application(root)
root.mainloop()