print("Porque para mim o viver é Cristo, e o morrer é ganho. Filipenses 1:21")

from tkinter import *
from tkinter.ttk import *
import pyautogui, keyboard, time, tkinter as tk
from threading import Thread

ak = tk.Tk()

class main:

    def __init__(ac, master=None):

        ac.fonteG = ("Arial", "10")
        ac.estb = "n"
        ac.hf = 0
        ac.cf = 10**99999
        ac.teclaf = "F1"
        ac.teclap = "F7"
        ac.val = False
        ac.clp = False

        ac.programa = Thread(target=ac.inicio, args=[])
        ac.clicando = Thread(target=ac.click, args=[])
        ac.pclicando = Thread(target=ac.pclick, args=[])

        ac.programa.start()
        ac.clicando.start()
        ac.pclicando.start()

    def inicio(ac, master=None):

        ac.fechar = False

        #Botão para Iniciar
        ac.b1 = ac.tecla()

        #Botão para Configurações
        ac.b2 = tk.Button(ak, text = "Configurações", height = 6, width = 30)
        ac.b2["command"] = ac.cfgs

        #Botão para Sair
        ac.b3 = tk.Button(ak, text = "Sair", height = 6, width = 30)
        ac.b3["command"] = ac.sair

        ac.b2.pack()
        ac.b3.pack()

    def tecla(ac):

        ac.val = True

        ac.tecla1 = tk.Button(ak, text = "Pressione %s ou Clique para Iniciar" % ac.teclaf, height = 6, width = 30)
        ac.tecla1["command"] = ac.script
        ac.tecla1.pack()

    def click(ac, master=None):

        while ac.fechar == False:
            try:
                if keyboard.is_pressed(ac.teclaf):
                    ac.script()

            except:
                quit(ac.click)

    def pclick(ac, master=None):

        while ac.fechar == False:
            try:
                if keyboard.is_pressed(ac.teclap):
                    ac.clp = True

            except:
                quit(ac.pclick)

    def cfgs(ac, master=None):

        ac.tecla1.destroy(), ac.b2.destroy(), ac.b3.destroy()

        #Tecla para iniciar Click
        ac.tlista1 = Label(ak, text = "Tecla para iniciar Auto-Click", font = ac.fonteG)
        ac.lista1 = Combobox(ak)
        ac.lista1['values'] = ("F1", "F2", "F3", "F4", "F5", "F6")
        ac.lista1.current(0)

        #Finitude de Clicks
        ac.tlista2 = Label(ak, text = "Quantidade de Clicks", font = ac.fonteG)
        ac.lista2 = Entry(ak, font = ac.fonteG)
        ac.lista2.insert(0, "0")

        #Congelamento de Mouse
        ac.tcs = BooleanVar()
        ac.tcs.set(False)
        ac.tc = Checkbutton(ak, text = "Mouse Congelado", var = ac.tcs)

        #Tempo Entre os Clicks
        ac.zero1 = IntVar()
        ac.zero1.set(0)
        ac.th1 = Label(ak, text = "Hor.", font = ac.fonteG)
        ac.h1 = Spinbox(ak, from_=0, to=100, width=5, textvariable=ac.zero1)
        ac.zero2 = IntVar()
        ac.zero2.set(0)
        ac.th2 = Label(ak, text = "Min.", font = ac.fonteG)
        ac.h2 = Spinbox(ak, from_=0, to=100, width=5, textvariable=ac.zero2)
        ac.zero3 = IntVar()
        ac.zero3.set(0)
        ac.th3 = Label(ak, text = "Seg.", font = ac.fonteG)
        ac.h3 = Spinbox(ak, from_=0, to=100, width=5, textvariable=ac.zero3)

        #Lista de Tecla para parar Click
        ac.tlista3 = Label(ak, text = "Tecla para parar Auto-Click", font = ac.fonteG)
        ac.lista3 = Combobox(ak)
        ac.lista3['values'] = ("F7", "F8", "F9", "F10", "F11", "F12")
        ac.lista3.current(0)

        #Voltar ao Início
        ac.b1 = tk.Button(ak, text="Confirmar Alterações", height=2, width=20)
        ac.b1["command"] = ac.ecfgs

        #Packs
        ac.tlista1.pack()
        ac.lista1.pack()
        ac.tlista3.pack()
        ac.lista3.pack()
        ac.tlista2.pack()
        ac.lista2.pack()
        ac.tc.pack()
        ac.th1.pack()
        ac.h1.pack()
        ac.th2.pack()
        ac.h2.pack()
        ac.th3.pack()
        ac.h3.pack()
        ac.b1.pack()

    def ecfgs(ac):

        ac.teclaf = ac.lista1.get()

        ac.cf = int(ac.lista2.get())

        if ac.tcs.get() == True:
            ac.estb = "s"
        else:
            ac.estb = "n"

        ac.hf = int(ac.h1.get()) * 3600 + int(ac.h2.get()) * 60 + int(ac.h3.get())

        ac.teclap = ac.lista3.get()

        #Finalização dos Widgets de Configurações
        ac.tlista1.destroy(), ac.lista1.destroy(), ac.tlista2.destroy(), ac.lista2.destroy(), ac.tc.destroy(), ac.th1.destroy(), ac.h1.destroy()
        ac.tlista3.destroy(), ac.lista3.destroy(), ac.th2.destroy(), ac.h2.destroy(), ac.th3.destroy(), ac.h3.destroy(), ac.b1.destroy()

        ac.fechar = True
        ac.inicio()

    def script(ac):

        ac.con = 0

        if ac.val == True:

            ac.pdc = pyautogui.position()

            while ac.con <= ac.cf:
                ac.con += 1

                if ac.estb == "s":
                    pyautogui.click(ac.pdc)
                    pyautogui.moveTo(ac.pdc)
                elif ac.estb == "n":
                    pyautogui.click(pyautogui.position())

                time.sleep(int(ac.hf))

                if ac.clp == True:
                    break

            ac.clp = False

        else:
            pass

    def destroy(ac, de):

        ac.de = de
        ac.de.destroy()
        Button(ac.de, text="Destroy", command=destroy, bg="white").pack()

    def sair(ac):

        ac.fechar = True
        quit()

main(ak)
ak.geometry("250x310")
ak.resizable(width=False, height=False)
ak.title("Auto-Click")
ak.mainloop()
