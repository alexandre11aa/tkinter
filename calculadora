print("Porque para mim o viver é Cristo, e o morrer é ganho. Filipenses 1:21")

from tkinter import *
import tkinter as tk

calculadora = tk.Tk()

class main:
    def __init__(ca, master=None):
        ca.conta = []
        ca.dig = ""
        ca.tela()

    def tela(ca):

        #Configuração dos elementos da calculadora
        ca.barra = Entry(calculadora, font = ("Arial", "10"))
        ca.barra.insert(0, str(ca.dig))

        ca.zero = tk.Button(calculadora, text= "0", command=ca.z)
        ca.um = tk.Button(calculadora, text = "1", command=ca.u)
        ca.dois = tk.Button(calculadora, text = "2", command=ca.d)
        ca.tres = tk.Button(calculadora, text="3", command=ca.t)
        ca.quatro = tk.Button(calculadora, text="4", command=ca.q)
        ca.cinco = tk.Button(calculadora, text="5", command=ca.cin)
        ca.seis = tk.Button(calculadora, text="6", command=ca.s)
        ca.sete = tk.Button(calculadora, text="7", command=ca.ss)
        ca.oito = tk.Button(calculadora, text="8", command=ca.o)
        ca.nove = tk.Button(calculadora, text="9", command=ca.n)

        ca.mais = tk.Button(calculadora, text="+", command=ca.ma)
        ca.menos = tk.Button(calculadora, text="-", command=ca.me)
        ca.mult = tk.Button(calculadora, text="*", command=ca.vz)
        ca.div = tk.Button(calculadora, text="/", command=ca.dv)
        ca.ele = tk.Button(calculadora, text="^", command=ca.el)

        ca.ponto = tk.Button(calculadora, text=".", command=ca.po)
        ca.limpar = tk.Button(calculadora, text="L", command=ca.li)
        ca.sair = tk.Button(calculadora, text="S", fg="red", command=ca.sa)

        ca.igual = tk.Button(calculadora, text="=",command=ca.ig)
        ca.apagar = tk.Button(calculadora, text="<", command=ca.ap)

        # Configuração do layout da calculadora
        ca.barra.grid(row=0, column=0, padx=10, pady=10, ipadx=80, ipady=5, columnspan=5)

        ca.sete.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=1)
        ca.oito.grid(row=1, column=1, padx=10, pady=10, ipadx=20, ipady=1)
        ca.nove.grid(row=1, column=2, padx=10, pady=10, ipadx=20, ipady=1)
        ca.mais.grid(row=1, column=3, padx=10, pady=10, ipadx=20, ipady=1)

        ca.quatro.grid(row=2, column=0, padx=10, pady=10, ipadx=20, ipady=1)
        ca.cinco.grid(row=2, column=1, padx=10, pady=10, ipadx=20, ipady=1)
        ca.seis.grid(row=2, column=2, padx=10, pady=10, ipadx=20, ipady=1)
        ca.menos.grid(row=2, column=3, padx=10, pady=10, ipadx=20, ipady=1)

        ca.um.grid(row=3, column=0, padx=10, pady=10, ipadx=20, ipady=1)
        ca.dois.grid(row=3, column=1, padx=10, pady=10, ipadx=20, ipady=1)
        ca.tres.grid(row=3, column=2, padx=10, pady=10, ipadx=20, ipady=1)
        ca.mult.grid(row=3, column=3, padx=10, pady=10, ipadx=20, ipady=1)

        ca.ponto.grid(row=4, column=0, padx=10, pady=10, ipadx=20, ipady=1)
        ca.zero.grid(row=4, column=1, padx=10, pady=10, ipadx=20, ipady=1)
        ca.ele.grid(row=4, column=2, padx=10, pady=10, ipadx=20, ipady=1)
        ca.div.grid(row=4, column=3, padx=10, pady=10, ipadx=20, ipady=1)

        ca.igual.grid(row=5, column=0, padx=10, pady=10, ipadx=20, ipady=1)
        ca.apagar.grid(row=5, column=1, padx=10, pady=10, ipadx=20, ipady=1)
        ca.limpar.grid(row=5, column=2, padx=10, pady=10, ipadx=20, ipady=1)
        ca.sair.grid(row=5, column=3, padx=10, pady=10, ipadx=20, ipady=1)

    #Ativação dos botões
    def z(ca):
        ca.conta.append("0")
        ca.juncao()
    def u(ca):
        ca.conta.append("1")
        ca.juncao()
    def d(ca):
        ca.conta.append("2")
        ca.juncao()
    def t(ca):
        ca.conta.append("3")
        ca.juncao()
    def q(ca):
        ca.conta.append("4")
        ca.juncao()
    def cin(ca):
        ca.conta.append("5")
        ca.juncao()
    def s(ca):
        ca.conta.append("6")
        ca.juncao()
    def ss(ca):
        ca.conta.append("7")
        ca.juncao()
    def o(ca):
        ca.conta.append("8")
        ca.juncao()
    def n(ca):
        ca.conta.append("9")
        ca.juncao()
    def po(ca):
        ca.conta.append(".")
        ca.juncao()

    def ma(ca):
        if len(ca.conta) == 0:
            ca.conta.append("0 + ")
            ca.juncao()
        elif ca.conta[len(ca.conta) - 1] == "+" or ca.conta[len(ca.conta) - 1] == "-" or ca.conta[len(ca.conta) - 1] == "*" \
                or ca.conta[len(ca.conta) - 1] == "/" or ca.conta[len(ca.conta) - 1] == "**" or ca.conta[len(ca.conta) - 1] == "0 + " \
                or ca.conta[len(ca.conta) - 1] == "0 - " or ca.conta[len(ca.conta) - 1] == "0 * " or ca.conta[len(ca.conta) - 1] == "0 / " \
                or ca.conta[len(ca.conta) - 1] == "0 ** ":
            ca.conta[len(ca.conta) - 1] = "+"
        else:
            ca.conta.append("+")
            ca.juncao()

    def me(ca):
        if len(ca.conta) == 0:
            ca.conta.append("0 - ")
            ca.juncao()
        elif ca.conta[len(ca.conta) - 1] == "+" or ca.conta[len(ca.conta) - 1] == "*" or ca.conta[len(ca.conta) - 1] == "/" \
                or ca.conta[len(ca.conta) - 1] == "**" or ca.conta[len(ca.conta) - 1] == "-" or ca.conta[len(ca.conta) - 1] == "0 + " \
                or ca.conta[len(ca.conta) - 1] == "0 - " or ca.conta[len(ca.conta) - 1] == "0 * " or ca.conta[len(ca.conta) - 1] == "0 / " \
                or ca.conta[len(ca.conta) - 1] == "0 ** ":
            ca.conta[len(ca.conta) - 1] = "-"
        else:
            ca.conta.append("-")
            ca.juncao()

    def dv(ca):
        if len(ca.conta) == 0:
            ca.conta.append("0 / ")
            ca.juncao()
        elif ca.conta[len(ca.conta) - 1] == "-" or ca.conta[len(ca.conta) - 1] == "*" or ca.conta[len(ca.conta) - 1] == "+" \
                or ca.conta[len(ca.conta) - 1] == "**" or ca.conta[len(ca.conta) - 1] == "/" or ca.conta[len(ca.conta) - 1] == "0 + " \
                or ca.conta[len(ca.conta) - 1] == "0 - " or ca.conta[len(ca.conta) - 1] == "0 * " or ca.conta[len(ca.conta) - 1] == "0 / " \
                or ca.conta[len(ca.conta) - 1] == "0 ** ":
            ca.conta[len(ca.conta) - 1] = "/"
        else:
            ca.conta.append("/")
            ca.juncao()

    def vz(ca):
        if len(ca.conta) == 0:
            ca.conta.append("0 * ")
            ca.juncao()
        elif ca.conta[len(ca.conta) - 1] == "-" or ca.conta[len(ca.conta) - 1] == "+" or ca.conta[len(ca.conta) - 1] == "/" \
                or ca.conta[len(ca.conta) - 1] == "**" or ca.conta[len(ca.conta) - 1] == "*" or ca.conta[len(ca.conta) - 1] == "0 + " \
                or ca.conta[len(ca.conta) - 1] == "0 - " or ca.conta[len(ca.conta) - 1] == "0 * " or ca.conta[len(ca.conta) - 1] == "0 / " \
                or ca.conta[len(ca.conta) - 1] == "0 ** ":
            ca.conta[len(ca.conta) - 1] = "*"
        else:
            ca.conta.append("*")
            ca.juncao()

    def el(ca):
        if len(ca.conta) == 0:
            ca.conta.append("0 ** ")
            ca.juncao()
        elif ca.conta[len(ca.conta) - 1] == "-" or ca.conta[len(ca.conta) - 1] == "*" or ca.conta[len(ca.conta) - 1] == "/" \
                or ca.conta[len(ca.conta) - 1] == "+" or ca.conta[len(ca.conta) - 1] == "**" or ca.conta[len(ca.conta) - 1] == "0 + " \
                or ca.conta[len(ca.conta) - 1] == "0 - " or ca.conta[len(ca.conta) - 1] == "0 * " or ca.conta[len(ca.conta) - 1] == "0 / " \
                or ca.conta[len(ca.conta) - 1] == "0 ** ":
            ca.conta[len(ca.conta) - 1] = "**"
        else:
            ca.conta.append("**")
            ca.juncao()

    #Junção das teclas dos botões
    def juncao(ca):
        if ca.conta[len(ca.conta) - 1] == "+" or ca.conta[len(ca.conta) - 1] == "-" or ca.conta[len(ca.conta) - 1] == "/" \
                or ca.conta[len(ca.conta) - 1] == "*" or ca.conta[len(ca.conta) - 1] == "**":
            ca.dig += " " + ca.conta[len(ca.conta) - 1] + " "
        else:
            ca.dig += ca.conta[len(ca.conta) - 1]

        ca.tela()

    #Cálculo
    def ig(ca):
        #Tratamento das teclas ativadas
        ca.dig = ""

        ca.en = str(ca.barra.get())

        ca.en = ca.en.split()

        ca.c = 0
        ca.ent = ""

        while ca.c < len(ca.en):
            ca.ent += str(ca.en[ca.c])
            ca.c += 1

            if ca.ent[0] == "+" or ca.ent[0] == "-" or ca.ent[0] == "/" or ca.ent[0] == "*" or ca.ent[0] == "**":
                ca.ent = "0" + ca.ent

        ca.c = 0
        ca.dig = ""

        #Tratamento das notações científicas
        ca.val = 0

        while ca.c < len(ca.ent):
            if ca.ent[ca.c] == "+" or ca.ent[ca.c] == "-" or ca.ent[ca.c] == "/" or ca.ent[ca.c] == "*" or ca.ent[ca.c] == "**":
                if ca.ent[ca.c - 1] != "e":
                    ca.dig += " " + str(ca.ent[ca.c]) + " "
                else:
                    ca.dig += str(ca.ent[ca.c])
            else:
                ca.dig += str(ca.ent[ca.c])

            ca.c += 1

        ca.c = 0

        while ca.c < len(ca.dig):
            ca.ent = ""
            if ca.dig[ca.c] == "e":
                if ca.dig[ca.c + 1] == "+":
                    ca.dig1 = ca.dig.split("e+")
                    ca.c1 = 0
                    ca.val = 1
                    while ca.c1 < len(ca.dig1):
                        ca.ent += ca.dig1[ca.c1]
                        if ca.c1 < len(ca.dig1) - 1:
                            ca.ent += " * " + str(10 ** int((ca.dig1[ca.c1 + 1]).split()[0])) + " "
                            ca.c2 = 1
                            ca.dig2 = ""

                            while ca.c2 < len((ca.dig1[ca.c1 + 1]).split()):
                                if ca.c2 < len((ca.dig1[ca.c1 + 1]).split()) - 1:
                                    ca.dig2 += ((ca.dig1[ca.c1 + 1]).split())[ca.c2] + " "
                                    ca.c2 += 1
                                else:
                                    ca.dig2 += ((ca.dig1[ca.c1 + 1]).split())[ca.c2]
                                    ca.c2 += 1

                            ca.dig1[ca.c1 + 1] = ca.dig2

                        ca.c1 += 1

                    break

            ca.c += 1

        ca.c = 0

        while ca.c < len(ca.ent):
            ca.dig = ""
            if ca.ent[ca.c] == "e":
                if ca.ent[ca.c + 1] == "-":
                    ca.dig1 = ca.ent.split("e-")
                    ca.c1 = 0
                    ca.val = 0
                    while ca.c1 < len(ca.dig1):
                        ca.dig += ca.dig1[ca.c1]
                        if ca.c1 < len(ca.dig1) - 1:
                            ca.dig += " / " + str(10 ** int((ca.dig1[ca.c1 + 1]).split()[0])) + " "
                            ca.c2 = 1
                            ca.dig2 = ""

                            while ca.c2 < len((ca.dig1[ca.c1 + 1]).split()):
                                if ca.c2 < len((ca.dig1[ca.c1 + 1]).split()) - 1:
                                    ca.dig2 += ((ca.dig1[ca.c1 + 1]).split())[ca.c2] + " "
                                    ca.c2 += 1
                                else:
                                    ca.dig2 += ((ca.dig1[ca.c1 + 1]).split())[ca.c2]
                                    ca.c2 += 1

                            ca.dig1[ca.c1 + 1] = ca.dig2

                        ca.c1 += 1

                    break

            ca.c += 1

        if ca.val == 1:
            ca.resultado = ca.ent.split()
        else:
            ca.resultado = ca.dig.split()

        ca.c = 0

        #Verificação de Erro
        ca.c = 1
        ca.dig = ca.resultado[0]

        while ca.c < len(ca.resultado):
            if ca.c < len(ca.resultado) - 1:
                ca.dig += " " + ca.resultado[ca.c] + " "
                ca.c += 1
            else:
                ca.dig += " " + ca.resultado[ca.c]
                ca.c += 1

        ca.dig = str(eval(ca.dig))
        ca.conta = [str(eval(ca.dig))]

        ca.tela()

    def error(ca):
        ca.resultado = ["0"]

    #Delete da última tecla ativada na lista
    def li(ca):
        ca.dig = ""
        ca.conta = [ca.dig]

        ca.tela()

    #Limpeza da lista de teclas ativadas
    def ap(ca):
        if len(ca.conta) != 0:
            ca.conta.pop()
            ca.c = 0
            ca.dig = ""

            while ca.c < (len(ca.conta)):
                if ca.conta[ca.c] == "+" or ca.conta[ca.c] == "-" or ca.conta[ca.c] == "/" or ca.conta[ca.c] == "*" \
                        or ca.conta[ca.c] == "**":
                    ca.dig += " " + ca.conta[len(ca.conta) - 1] + " "
                    ca.c += 1
                else:
                    ca.dig += ca.conta[ca.c]
                    ca.c += 1

            ca.tela()

        else:
            pass

    def sa(ca):
        quit()

main(calculadora)
calculadora.resizable(width=False, height=False)
calculadora.title("Calculadora")
calculadora.mainloop()
