print("Porque para mim o viver é Cristo, e o morrer é ganho. Filipenses 1:21")

from tkinter import *
from tkinter.ttk import *
import tkinter as tk

conversor = tk.Tk()

class main:
    def __init__(co, master=None):
        co.fonteG = ("Arial", "10")
        co.resultadoP, co.Presultado = [0, 0]
        co.tipoP, co.Ptipo, co.rtP, co.Prt = ["","",2,2]
        co.fixoP, co.Pfixo, co.boxP, co.Pbox = [0,0,0,0]

        co.tela()

    def tela(co):

        #--- Configurações da Tela ---

        #...para Decimal
        co.Pdec = tk.Button(conversor, text="Decimal ← ", font=co.fonteG, command=co.Pescolha)

        co.Pl = Combobox(conversor, values=("Binário", "Octal", "Hexadecimal"))
        co.Pl.current(co.Pbox)

        co.Pn = tk.Label(conversor,borderwidth=1,width=17,relief="raised",text=str(co.Presultado),font=co.fonteG)

        co.Pr = Entry(conversor, font=co.fonteG)
        co.Pr.insert(0,str(co.Pfixo))

        #Decimal para...
        co.decP = tk.Button(conversor, text="Decimal → ", font=co.fonteG, command=co.escolhaP)

        co.lP = Combobox(conversor, values=("Binário", "Octal", "Hexadecimal"))
        co.lP.current(co.boxP)

        co.nP = Entry(conversor, font=co.fonteG)
        co.nP.insert(0, co.fixoP)

        co.rP = tk.Label(conversor,borderwidth=1,width=17,relief="raised",text=str(co.resultadoP),font=co.fonteG)

        #Sair
        co.ss = tk.Button(conversor, text="Sair", font=co.fonteG, fg="red", command=co.sair)

        #--- Interações do Usuário ---

        #...para Decimal
        co.Pdec.grid(row=4, column=0, padx=2, pady=2, ipadx=43, ipady=0, columnspan=5)
        co.Pl.grid(row=4, column=5, padx=2, pady=2, ipadx=10, ipady=3, columnspan=5)

        co.Pn.grid(row=5, column=0, padx=1, pady=2, ipadx=10, ipady=2, columnspan=5)
        co.Pr.grid(row=5, column=5, padx=2, pady=2, ipadx=10, ipady=2, columnspan=5)

        #Espaço
        co.esp2 = tk.Label(conversor, borderwidth=1, width=41, relief="ridge", font=co.fonteG)
        co.esp2.grid(row=6, column=1, padx=2, pady=2, ipadx=1, ipady=1, columnspan=5)

        #Decimal para..
        co.decP.grid(row=0, column=0, padx=2, pady=2, ipadx=43, ipady=0, columnspan=5)
        co.lP.grid(row=0, column=5, padx=2, pady=2, ipadx=10, ipady=3, columnspan=5)

        co.nP.grid(row=1, column=0, padx=1, pady=2, ipadx=10, ipady=2, columnspan=5)
        co.rP.grid(row=1, column=5, padx=2, pady=2, ipadx=10, ipady=2, columnspan=5)

        #Espaço
        co.esp1 = tk.Label(conversor, borderwidth=1, width=41, relief="ridge", font=co.fonteG)
        co.esp1.grid(row=3, column=1, padx=2, pady=2, ipadx=1, ipady=1, columnspan=5)

        #Sair
        co.ss.grid(row=7, column=1, padx=2, pady=2, ipadx=150, ipady=0, columnspan=5)

    def escolhaP(co):
        co.ntP = co.nP.get()
        co.tipoP = co.lP.get()
        co.fixoP = co.ntP

        if co.tipoP == "Binário":
            co.rtP = 2
            co.boxP = 0
        elif co.tipoP == "Octal":
            co.rtP = 8
            co.boxP = 1
        elif co.tipoP == "Hexadecimal":
            co.rtP = 16
            co.boxP = 2

        co.verificarP()

    def verificarP(co):
        co.con = 0
        co.val = 0

        while co.con < len(str(co.ntP)):
            if str(str(co.ntP)[co.con]) != "0" and str(str(co.ntP)[co.con]) != "1" and str(str(co.ntP)[co.con]) != "2" and \
                    str(str(co.ntP)[co.con]) != "3" and str(str(co.ntP)[co.con]) != "4" and str(str(co.ntP)[co.con]) != "5" and \
                    str(str(co.ntP)[co.con]) != "6" and str(str(co.ntP)[co.con]) != "7" and str(str(co.ntP)[co.con]) != "8" and \
                    str(str(co.ntP)[co.con]) != "9":
                co.val = 1
                co.erroP()
                break

            co.con += 1

        if co.val == 0:
            co.calP()

    def calP(co):
        co.resultadoP = ""

        while True:
            if int(co.ntP) < int(co.rtP):
                if int(float(co.ntP)) < 10:
                    co.resultadoP = str(int(float(co.ntP))) + co.resultadoP
                    break
                elif int(float(co.ntP)) == 10:
                    co.resultadoP = "A" + co.resultadoP
                    break
                elif int(float(co.ntP)) == 11:
                    co.resultadoP = "B" + co.resultadoP
                    break
                elif int(float(co.ntP)) == 12:
                    co.resultadoP = "C" + co.resultadoP
                    break
                elif int(float(co.ntP)) == 13:
                    co.resultadoP = "D" + co.resultadoP
                    break
                elif int(float(co.ntP)) == 14:
                    co.resultadoP = "E" + co.resultadoP
                    break
                else:
                    co.resultadoP = "F" + co.resultadoP
                    break

            if int(float(co.ntP) % float(co.rtP)) < 10:
                co.resultadoP = str(int(float(co.ntP) % float(co.rtP))) + co.resultadoP
            elif int(float(co.ntP) % float(co.rtP)) == 10:
                co.resultadoP = "A" + co.resultadoP
            elif int(float(co.ntP) % float(co.rtP)) == 11:
                co.resultadoP = "B" + co.resultadoP
            elif int(float(co.ntP) % float(co.rtP)) == 12:
                co.resultadoP = "C" + co.resultadoP
            elif int(float(co.ntP) % float(co.rtP)) == 13:
                co.resultadoP = "D" + co.resultadoP
            elif int(float(co.ntP) % float(co.rtP)) == 14:
                co.resultadoP = "E" + co.resultadoP
            else:
                co.resultadoP = "F" + co.resultadoP

            co.ntP = int(float(co.ntP) / float(co.rtP))

        co.tela()

    def Pescolha(co):
        co.Pnt = co.Pr.get()
        co.Ptipo = co.Pl.get()
        co.Pfixo = str(co.Pnt)

        if co.Ptipo == "Binário":
            co.Prt = 2
            co.Pbox = 0
        elif co.Ptipo == "Octal":
            co.Prt = 8
            co.Pbox = 1
        elif co.Ptipo == "Hexadecimal":
            co.Prt = 16
            co.Pbox = 2

        co.Pverificar()

    def Pverificar(co):
        co.con = 0
        co.val = 0
        co.va2 = 0

        if co.Prt == 2 or co.Prt == 8:
            while co.con < len(str(co.Pnt)):
                if str(str(co.Pnt)[co.con]) != "0" and str(str(co.Pnt)[co.con]) != "1" and str(str(co.Pnt)[co.con]) != "2" and \
                        str(str(co.Pnt)[co.con]) != "3" and str(str(co.Pnt)[co.con]) != "4" and str(str(co.Pnt)[co.con]) != "5" and \
                        str(str(co.Pnt)[co.con]) != "6" and str(str(co.Pnt)[co.con]) != "7" and str(str(co.Pnt)[co.con]) != "8" and \
                        str(str(co.Pnt)[co.con]) != "9":
                    co.val = 1
                    co.va2 = 1
                    co.Perro()
                    break

                co.con += 1

        elif co.Prt == 16:
            while co.con < len(str(co.Pnt)):
                if str(str(co.Pnt)[co.con]) != "0" and str(str(co.Pnt)[co.con]) != "1" and str(str(co.Pnt)[co.con]) != "2" and \
                        str(str(co.Pnt)[co.con]) != "3" and str(str(co.Pnt)[co.con]) != "4" and str(str(co.Pnt)[co.con]) != "5" and \
                        str(str(co.Pnt)[co.con]) != "6" and str(str(co.Pnt)[co.con]) != "7" and str(str(co.Pnt)[co.con]) != "8" and \
                        str(str(co.Pnt)[co.con]) != "9" and str(str(co.Pnt)[co.con]) != "A" and str(str(co.Pnt)[co.con]) != "B" and \
                        str(str(co.Pnt)[co.con]) != "C" and str(str(co.Pnt)[co.con]) != "D" and str(str(co.Pnt)[co.con]) != "E" and \
                        str(str(co.Pnt)[co.con]) != "F":
                    co.val = 1
                    co.va2 = 1
                    co.Perro()
                    break

                co.con += 1

        co.con = 0

        if co.Prt == 2 and co.va2 == 0:
            while co.con < len(str(co.Pnt)):
                if int(str(co.Pnt)[co.con]) > 1:
                    co.val = 1
                    co.Perro()
                    break

                co.con += 1

        elif co.Prt == 8 and co.va2 == 0:
            while co.con < len(str(co.Pnt)):
                if int(str(co.Pnt)[co.con]) > 7:
                    co.val = 1
                    co.Perro()
                    break

                co.con += 1

        if co.val == 0:
            co.Pcal()

    def Pcal(co):
        co.con = 0
        co.Presultado = 0

        while co.con < len(str(co.Pnt)):
            if str(co.Pnt)[co.con] == "A":
                co.Presultado += 10 * int(co.Prt) ** (len(str(co.Pnt)) - co.con - 1)
            elif str(co.Pnt)[co.con] == "B":
                co.Presultado += 11 * int(co.Prt) ** (len(str(co.Pnt)) - co.con - 1)
            elif str(co.Pnt)[co.con] == "C":
                co.Presultado += 12 * int(co.Prt) ** (len(str(co.Pnt)) - co.con - 1)
            elif str(co.Pnt)[co.con] == "D":
                co.Presultado += 13 * int(co.Prt) ** (len(str(co.Pnt)) - co.con - 1)
            elif str(co.Pnt)[co.con] == "E":
                co.Presultado += 14 * int(co.Prt) ** (len(str(co.Pnt)) - co.con - 1)
            elif str(co.Pnt)[co.con] == "F":
                co.Presultado += 15 * int(co.Prt) ** (len(str(co.Pnt)) - co.con - 1)
            else:
                co.Presultado += int(str(co.Pnt)[co.con]) * int(co.Prt) ** (len(str(co.Pnt)) - co.con - 1)

            co.con += 1

        co.tela()

    def erroP(co):
        co.resultadoP = "NaN"

        co.tela()
    def Perro(co):
        co.Presultado = "NaN"
        co.tela()

    def sair(co):
        quit()

main(conversor)
conversor.resizable(width=False, height=False)
conversor.title("Conversor Decimal")
conversor.mainloop()
