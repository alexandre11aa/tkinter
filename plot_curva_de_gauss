print("Porque para mim o viver é Cristo, e o morrer é ganho. Filipenses 1:21")

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

p_cgauss = tk.Tk()

class main:
    def __init__(pcg, master=None):
        pcg.fonteG = ("Arial", "10")
        pcg.ini = "0"
        pcg.fin = "0"
        pcg.qtd = "1"

        pcg.tela()

    def tela(pcg):

        # --- Configurações da Tela ---

        pcg.inicio = tk.Label(p_cgauss, borderwidth=1, width=17, relief="raised", text="Intervalo Inicial", font=pcg.fonteG)
        pcg.final = tk.Label(p_cgauss, borderwidth=1, width=17, relief="raised", text="Intervalo Final", font=pcg.fonteG)
        pcg.quantidade = tk.Label(p_cgauss, borderwidth=1, width=17, relief="raised", text="N. de Gráficos",font=pcg.fonteG)

        pcg.t_ini = Entry(p_cgauss, font=pcg.fonteG)
        pcg.t_ini.insert(0,pcg.ini)

        pcg.t_fin = Entry(p_cgauss, font=pcg.fonteG)
        pcg.t_fin.insert(0,pcg.fin)

        pcg.t_qtd = Entry(p_cgauss, font=pcg.fonteG)
        pcg.t_qtd.insert(0,pcg.qtd)

        pcg.plot = tk.Button(p_cgauss, text="Gerar", font=pcg.fonteG, fg="black", command=pcg.variaveis)
        pcg.test = tk.Button(p_cgauss, text="Teste", font=pcg.fonteG, fg="black", command=pcg.teste)
        pcg.ss = tk.Button(p_cgauss, text="Sair", font=pcg.fonteG, fg="red", command=pcg.sair)

        #--- Interações do Usuário ---

        pcg.inicio.grid(row=1, column=1, padx=2, pady=2, ipadx=6, ipady=3, columnspan=2)
        pcg.final.grid(row=1, column=3, padx=2, pady=2, ipadx=6, ipady=3, columnspan=2)
        pcg.quantidade.grid(row=1, column=5, padx=2, pady=2, ipadx=6, ipady=3, columnspan=2)

        pcg.t_ini.grid(row=2, column=1, padx=1, pady=2, ipadx=2, ipady=1, columnspan=2)
        pcg.t_fin.grid(row=2, column=3, padx=1, pady=2, ipadx=2, ipady=1, columnspan=2)
        pcg.t_qtd.grid(row=2, column=5, padx=1, pady=2, ipadx=2, ipady=1, columnspan=2)

        pcg.plot.grid(row=4, column=1, padx=1, pady=2, ipadx=53, ipady=1, columnspan=2)
        pcg.test.grid(row=4, column=3, padx=1, pady=2, ipadx=53, ipady=1, columnspan=2)
        pcg.ss.grid(row=4, column=5, padx=1, pady=2, ipadx=58, ipady=1, columnspan=2)

    def variaveis(pcg):
        pcg.v_ini = pcg.t_ini.get().split()
        pcg.v_fin = pcg.t_fin.get().split()
        pcg.v_qtd = int(pcg.t_qtd.get())

        pcg.gerador()

    def gerador(pcg):
        pcg.matriz = []

        fig, pcg.matriz = plt.subplots(pcg.v_qtd)
        plt.style.use('fivethirtyeight')
        fig.suptitle('Curva de Gauss')

        pcg.x = np.arange(-10, 10, 0.001)
        pcg.y = norm.pdf(pcg.x, 0, 1)

        for i in range(pcg.v_qtd):
            pcg.z1 = float(pcg.v_ini[i])
            pcg.z2 = float(pcg.v_fin[i])

            pcg.x_z = np.arange(pcg.z1, pcg.z2, 0.001)
            pcg.y_z = norm.pdf(pcg.x_z, 0, 1)

            pcg.matriz[i].plot(pcg.x, pcg.y)

            pcg.matriz[i].fill_between(pcg.x_z, pcg.y_z, 0, alpha=0.1, color='b')
            pcg.matriz[i].fill_between(pcg.x, pcg.y, 0, alpha=0.3)
            pcg.matriz[i].set_xlim([-4, 4])
            pcg.matriz[i].set_xlabel('Gráfico ' + str(i + 1))
            pcg.matriz[i].set_yticklabels([])

        janela = plt.get_current_fig_manager()
        janela.window.state('zoomed')
        plt.savefig('normal_curve.png', dpi=72, bbox_inches='tight')
        plt.show()

    def teste(pcg):
        pcg.ini = "-2.2 -1 2.2"
        pcg.fin = "0 1 4.2"
        pcg.qtd = "3"

        pcg.tela()

    def sair(pcg):
        quit()

main(p_cgauss)
p_cgauss.resizable(width=False, height=False)
p_cgauss.title("Curva de Gauss")
p_cgauss.mainloop()
