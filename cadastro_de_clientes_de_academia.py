print("Porque para mim o viver é Cristo, e o morrer é ganho. Filipenses 1:21")

from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from datetime import date
import sqlite3

root = tix.Tk()

class funcoes():

    # Banco de Dados
    def c_bancodd(cdc):
        cdc.cnct = sqlite3.connect("clientes.bd")
        cdc.mouse = cdc.cnct.cursor(); print("\nConectando ao banco de dados.")
    def d_bancodd(cdc):
        cdc.cnct.close(); print("\nDesconectando do banco de dados.")
    def tabelas(cdc):
        cdc.c_bancodd()

        # Criando Tabelas:
        cdc.mouse.execute("""
            CREATE TABLE IF NOT EXISTS clientes 
            (
                cod INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                diaM INTEGER(20),
                mesM INTEGER(20),
                anoM INTEGER(20),
                rua CHAR(40), 
                numero INTEGER(20), 
                bairro CHAR(40), 
                telefone INTEGER(20),
                sexo CHAR(40),
                diaV INTEGER(20),
                mesV INTEGER(20),
                anoV INTEGER(20), 
                idade INTEGER(20),
                peso INTEGER(20), 
                altura INTEGER(20)
            );
        """)

        cdc.cnct.commit(); print("\nBanco de dados criado com sucesso.")
        cdc.d_bancodd()

    # Variáveis
    def variaveis(cdc):
        cdc.id = cdc.id_e.get()
        cdc.diaM = cdc.mesM_e.get()
        cdc.mesM = cdc.diaM_e.get()
        cdc.anoM = cdc.anoM_e.get()
        cdc.nome = cdc.nome_e.get()
        cdc.rua = cdc.rua_e.get()
        cdc.num = cdc.num_e.get()
        cdc.bairro = cdc.bairro_e.get()
        cdc.tel = cdc.tel_e.get()
        cdc.sexo = cdc.sexo_V.get()
        cdc.diaV = cdc.mesV_e.get()
        cdc.mesV = cdc.diaV_e.get()
        cdc.anoV = cdc.anoV_e.get()
        cdc.idade = cdc.idade_e.get()
        cdc.peso = cdc.peso_e.get()
        cdc.altura = cdc.altura_e.get()

    # Variáveis do tempo
    def tempo(cdc):
        cdc.c_bancodd()

        try:
            cdc.d_e_atraso, cdc.stcao = ["",""]

            for i in cdc.lista_c.selection():
                col1, col2, col3, col4 = cdc.lista_c.item(i, 'values')

            cdc.id = col1
            m_vencimento = []

            lista_t = cdc.mouse.execute(''' SELECT diaV, mesV, anoV FROM clientes WHERE cod = ? ''', cdc.id)
            for i in lista_t:
                m_vencimento.append(i)

                d_atual = list(map(int,(str(date.today())).split("-")))

            if (m_vencimento[0][0] != "") and (m_vencimento[0][1] != "") and (m_vencimento[0][2] != ""):
                if (d_atual[0] >= int(m_vencimento[0][2])) and (d_atual[1] >= int(m_vencimento[0][0])) and (d_atual[2] >= int(m_vencimento[0][1])):
                    cdc.stcao = "Em Atraso"
                    cdc.d_e_atraso = str(((int(m_vencimento[0][2]) - d_atual[0]) * 365) + ((int(m_vencimento[0][0]) - d_atual[1]) * 30) + (d_atual[2] - int(m_vencimento[0][1])))
                else:
                    cdc.stcao = "Em Dia"
                    cdc.d_e_atraso = "0"
        except ValueError:
            pass

        cdc.d_bancodd()

    # Gasto Calórico por Harris-Benedict
    def g_c(cdc):
        cdc.c_bancodd()
        cdc.gasto = ""

        try:
            for i in cdc.lista_c.selection():
                col1, col2, col3, col4 = cdc.lista_c.item(i, 'values')

            cdc.id = col1
            m_variaveis = []

            lista_gc = cdc.mouse.execute(''' SELECT sexo, idade, peso, altura FROM clientes WHERE cod = ? ''', cdc.id)
            for i in lista_gc:
                m_variaveis.append(i)

            if (m_variaveis[0][0] != "") and (m_variaveis[0][1] != "") and (m_variaveis[0][2] != "") and (m_variaveis[0][3] != ""):
                estatura = ""
                for i in range(len(str(m_variaveis[0][3]))):
                    if str(m_variaveis[0][3])[i] == ",":
                        estatura += "."
                    else:
                        estatura += str(m_variaveis[0][3])[i]

                if (m_variaveis[0][0] == "Masculino"):
                    cdc.gasto = str((10 * float(m_variaveis[0][2])) + (6.25 * float(estatura)) - (5 * int(m_variaveis[0][1])) + 5)
                elif (m_variaveis[0][0] == "Feminino"):
                    cdc.gasto = str((10 * float(m_variaveis[0][2])) + (6.25 * float(estatura)) - (5 * int(m_variaveis[0][1])) - 161)

        except ValueError:
            pass

        cdc.d_bancodd()

    # Botão Limpar
    def limpando(cdc):
        # Aba 1
        cdc.id_e.delete(0, END)
        cdc.diaM_e.delete(0, END)
        cdc.mesM_e.delete(0, END)
        cdc.anoM_e.delete(0, END)
        cdc.nome_e.delete(0, END)
        cdc.rua_e.delete(0, END)
        cdc.num_e.delete(0, END)
        cdc.bairro_e.delete(0, END)
        cdc.tel_e.delete(0, END)
        cdc.sexo_V.set('')
        cdc.diaV_e.delete(0, END)
        cdc.mesV_e.delete(0, END)
        cdc.anoV_e.delete(0, END)
        cdc.idade_e.delete(0, END)
        cdc.peso_e.delete(0, END)
        cdc.altura_e.delete(0, END)

        # Aba 2
        cdc.id_d2.configure(text="")
        cdc.diaM_d2.configure(text="")
        cdc.mesM_d2.configure(text="")
        cdc.anoM_d2.configure(text="")
        cdc.nome_d2.configure(text="")
        cdc.rua_d2.configure(text="")
        cdc.num_d2.configure(text="")
        cdc.bairro_d2.configure(text="")
        cdc.tel_d2.configure(text="")
        cdc.sexo_d2.configure(text="")
        cdc.diaV_d2.configure(text="")
        cdc.mesV_d2.configure(text="")
        cdc.anoV_d2.configure(text="")
        cdc.idade_d2.configure(text="")
        cdc.peso_d2.configure(text="")
        cdc.altura_d2.configure(text="")
        cdc.situacao_d2.configure(text="")
        cdc.di_at_d2.configure(text="")
        cdc.tmb_d2.configure(text="")

    # Botão Buscar
    def buscando(cdc):
        cdc.c_bancodd()
        cdc.lista_c.delete(*cdc.lista_c.get_children())
        cdc.stcao_l = []

        cdc.nome_e.insert(END, "%")
        nme = cdc.nome_e.get()
        cdc.mouse.execute(
            """ SELECT cod, nome, telefone, diaV, mesV, anoV FROM clientes
            WHERE nome LIKE "%s" ORDER BY nome ASC """ % nme)
        busca = cdc.mouse.fetchall()

        d_atual_l = list(map(int, (str(date.today())).split("-")))

        for i in range(len(busca)):
            if (busca[i][5] != "") and (busca[i][3] != "") and (busca[i][4] != ""):
                if (d_atual_l[0] >= int(busca[i][5])) and (d_atual_l[1] >= int(busca[i][3])) and (d_atual_l[2] >= int(busca[i][4])):
                    cdc.stcao_l.append("Em Atraso")
                else:
                    cdc.stcao_l.append("Em Dia")
            else:
                cdc.stcao_l.append("")

        for i in range(len(busca)):
            cdc.lista_c.insert("", END, values=(busca[i][0], busca[i][1], busca[i][2], cdc.stcao_l[i]))

        cdc.limpando()
        cdc.d_bancodd()

    # Botão Salvar
    def f_salvar(cdc):
        try:
            cdc.variaveis()
            cdc.c_bancodd()

            cdc.mouse.execute(""" INSERT INTO clientes (cod, diaM, mesM, anoM, nome, rua, numero, bairro, telefone, sexo, diaV, mesV, anoV, idade, peso, altura) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """,
                                (cdc.id, cdc.diaM, cdc.mesM, cdc.anoM, cdc.nome, cdc.rua, cdc.num, cdc.bairro, cdc.tel, cdc.sexo, cdc.diaV, cdc.mesV, cdc.anoV, cdc.idade, cdc.peso, cdc.altura))

            cdc.cnct.commit()
            cdc.d_bancodd()
            cdc.sel_lista()
            cdc.limpando()

        except sqlite3.IntegrityError:
            msg = ' O campo do "ID" é deve ser preenchido obrigatóriamente.' \
                  ' \n      O campo "ID" não pode já estar registrado na lista.'
            messagebox.showinfo("Erro", msg)
    def sel_lista(cdc):
        cdc.c_bancodd()
        cdc.lista_c.delete(*cdc.lista_c.get_children())
        cdc.stcao_l = []

        m_v = []
        lista = cdc.mouse.execute(''' SELECT cod, nome, telefone, diaV, mesV, anoV FROM clientes ORDER BY nome ASC; ''')
        for i in lista:
            m_v.append(i)

        d_atual_l = list(map(int, (str(date.today())).split("-")))

        try:
            for i in range(len(m_v)):
                if (m_v[i][5] != "") and (m_v[i][3] != "") and (m_v[i][4] != ""):
                    if (d_atual_l[0] >= int(m_v[i][5])) and (d_atual_l[1] >= int(m_v[i][3])) and (d_atual_l[2] >= int(m_v[i][4])):
                        cdc.stcao_l.append("Em Atraso")
                    else:
                        cdc.stcao_l.append("Em Dia")
                else:
                    cdc.stcao_l.append("")

            for i in range(len(m_v)):
                cdc.lista_c.insert("", END, values=(m_v[i][0],m_v[i][1],m_v[i][2],cdc.stcao_l[i]))

        except ValueError:
            for i in range(len(m_v)):
                cdc.lista_c.insert("", END, values=(m_v[i][0],m_v[i][1],m_v[i][2],""))

        cdc.d_bancodd()

    # Botão Editar
    def editor(cdc):
        cdc.limpando()

        try:
            cdc.c_bancodd()

            for i in cdc.lista_c.selection():
                col1, col2, col3, col4 = cdc.lista_c.item(i, 'values')

                cdc.id = col1
                matriz = []

            lista_e = cdc.mouse.execute(''' SELECT cod, diaM, mesM, anoM, nome, rua, numero, bairro, telefone, sexo, diaV, mesV, anoV, idade, peso, altura FROM clientes WHERE cod = ? ''', cdc.id)
            for i in lista_e:
                matriz.append(i)

            cdc.id_e.insert(END, matriz[0][0])
            cdc.diaM_e.insert(END, matriz[0][2])
            cdc.mesM_e.insert(END, matriz[0][1])
            cdc.anoM_e.insert(END, matriz[0][3])
            cdc.nome_e.insert(END, matriz[0][4])
            cdc.rua_e.insert(END, matriz[0][5])
            cdc.num_e.insert(END, matriz[0][6])
            cdc.bairro_e.insert(END, matriz[0][7])
            cdc.tel_e.insert(END, matriz[0][8])
            cdc.sexo_V.set(matriz[0][9])
            cdc.diaV_e.insert(END, matriz[0][11])
            cdc.mesV_e.insert(END, matriz[0][10])
            cdc.anoV_e.insert(END, matriz[0][12])
            cdc.idade_e.insert(END, matriz[0][13])
            cdc.peso_e.insert(END, matriz[0][14])
            cdc.altura_e.insert(END, matriz[0][15])

            cdc.d_bancodd()
        except (AttributeError, sqlite3.ProgrammingError, UnboundLocalError):
            msg = ' Selecione algum cliente da lista.'
            messagebox.showinfo("Erro", msg)

    # Botão Alterar
    def alterando(cdc):
        cdc.variaveis()

        if cdc.id != "":
            cdc.c_bancodd()

            cdc.mouse.execute(""" UPDATE clientes SET nome = ?, diaM = ?, mesM = ?, anoM = ?, rua = ?, numero = ?, bairro = ?, telefone = ?, sexo = ?, diaV = ?, mesV = ?, anoV = ?, idade = ?, peso = ?, altura = ?
                WHERE cod = ? """, (cdc.nome, cdc.diaM, cdc.mesM, cdc.anoM, cdc.rua, cdc.num, cdc.bairro, cdc.tel, cdc.sexo, cdc.diaV, cdc.mesV, cdc.anoV, cdc.idade, cdc.peso, cdc.altura, cdc.id))
            cdc.cnct.commit()

            cdc.d_bancodd()
            cdc.sel_lista()
            cdc.limpando()
        else:
            msg = ' O campo do "ID" é deve ser preenchido obrigatóriamente.' \
                  ' \n                      Selecione algum cliente da lista.'
            messagebox.showinfo("Erro", msg)

    # Botão Apagar
    def f_apagar(cdc):
            cdc.editor()
            try:
                cdc.variaveis()
                cdc.c_bancodd()

                cdc.mouse.execute(""" DELETE FROM clientes WHERE cod = ? """, (cdc.id))
                cdc.cnct.commit()

                cdc.d_bancodd()
                cdc.sel_lista()
                cdc.limpando()
            except (AttributeError, sqlite3.ProgrammingError, UnboundLocalError):
                pass

    # Menu de Opções
    def menus(cdc):
        menub = Menu(cdc.root)
        cdc.root.config(menu=menub)

        file_m1 = Menu(menub)
        file_m2 = Menu(menub)

        def Quit(): cdc.root.destroy()

        menub.add_cascade(label='Opções', menu=file_m1)
        menub.add_cascade(label='Sobre ', menu=file_m2)

        file_m1.add_command(label='Sair   ', command=cdc.sair)
        file_m1.add_command(label='Limpar ', command=cdc.limpando)
        file_m2.add_command(label='Manual ', command=cdc.manual)

    # Opção Sair
    def sair(cdc):
        print("\nSaindo do programa...")
        quit()

    # Informações da aba Dados
    def inf_dados(cdc):
        try:
            cdc.limpando()
            cdc.tempo()
            cdc.g_c()
            cdc.c_bancodd()

            for i in cdc.lista_c.selection():
                col1, col2, col3, col4 = cdc.lista_c.item(i, 'values')

                cdc.id = col1
                matriz = []

            lista_e = cdc.mouse.execute(
                ''' SELECT cod, diaM, mesM, anoM, nome, rua, numero, bairro, telefone, sexo, diaV, mesV, anoV, idade, peso, altura FROM clientes WHERE cod = ? ''',
                cdc.id)
            for i in lista_e:
                matriz.append(i)

            cdc.id_d2.configure(text=str(matriz[0][0]))
            cdc.diaM_d2.configure(text=str(matriz[0][2]))
            cdc.mesM_d2.configure(text=str(matriz[0][1]))
            cdc.anoM_d2.configure(text=str(matriz[0][3]))
            cdc.nome_d2.configure(text=str(matriz[0][4]))
            cdc.rua_d2.configure(text=str(matriz[0][5]))
            cdc.num_d2.configure(text=str(matriz[0][6]))
            cdc.bairro_d2.configure(text=str(matriz[0][7]))
            cdc.tel_d2.configure(text=str(matriz[0][8]))
            cdc.sexo_d2.configure(text=str(matriz[0][9]))
            cdc.diaV_d2.configure(text=str(matriz[0][11]))
            cdc.mesV_d2.configure(text=str(matriz[0][10]))
            cdc.anoV_d2.configure(text=str(matriz[0][12]))
            cdc.idade_d2.configure(text=str(matriz[0][13]))
            cdc.peso_d2.configure(text=str(matriz[0][14]))
            cdc.altura_d2.configure(text=str(matriz[0][15]))
            cdc.situacao_d2.configure(text=cdc.stcao)
            cdc.di_at_d2.configure(text=cdc.d_e_atraso)
            cdc.tmb_d2.configure(text=cdc.gasto)

            cdc.d_bancodd()
        except UnboundLocalError:
            msg = ' Selecione algum cliente da lista.'
            messagebox.showinfo("Erro", msg)

class programa(funcoes):
    def __init__(cdc):
        cdc.root = root
        cdc.tela()
        cdc.frame_tela()
        cdc.apps_f1()
        cdc.apps_f2()
        cdc.tabelas()
        cdc.sel_lista()
        cdc.menus()
        root.mainloop()

    def tela(cdc):
        cdc.root.title("Cadastro de Clientes")
        cdc.root.configure(background='#A52A2A')
        cdc.root.geometry('1000x600')
        cdc.root.resizable(True, True)
        cdc.root.maxsize(width=1920, height=1080)
        cdc.root.minsize(width=1000, height=600)

    def frame_tela(cdc):
        cdc.frame1 = Frame(cdc.root, bd=0.1, bg='#dfe3ee',
                          highlightbackground='#B8860B', highlightthickness=2)
        cdc.frame1.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.45)

        cdc.frame2 = Frame(cdc.root, bd=0.1, bg='#dfe3ee',
                          highlightbackground='#B8860B', highlightthickness=2)
        cdc.frame2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.45)

    def apps_f1(cdc):
        # Configurações de Abas
        cdc.abas = ttk.Notebook(cdc.frame1)

        cdc.aba1 = Frame(cdc.abas)
        cdc.aba1.configure(background='#dfe3ee')
        cdc.abas.add(cdc.aba1, text = " Registro ")

        cdc.aba2 = Frame(cdc.abas)
        cdc.aba2.configure(background='#dfe3ee')
        cdc.abas.add(cdc.aba2, text = "   Dados  ")

        cdc.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        cdc.aba1_f()
        cdc.aba2_f()

    def aba1_f(cdc):
        # - ABA 1 -

        # Botões
        cdc.salvar = Button(cdc.aba1,text='SALVAR', bd=2, bg='#A52A2A', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.f_salvar)
        cdc.salvar.place(relx=0.025, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.salvar_balao = tix.Balloon(cdc.frame1)
        cdc.salvar_balao.bind_widget(cdc.salvar, balloonmsg = "Clique para salvar as informações digitadas.")

        cdc.editar = Button(cdc.aba1,text='EDITAR', bd=2, bg='#A52A2A', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.editor)
        cdc.editar.place(relx=0.155, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.editar_balao = tix.Balloon(cdc.frame1)
        cdc.editar_balao.bind_widget(cdc.editar, balloonmsg="Clique para editar as informações selecionadas.")

        cdc.alterar = Button(cdc.aba1,text='ALTERAR', bd=2, bg='#A52A2A', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.alterando)
        cdc.alterar.place(relx=0.285, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.alterar_balao = tix.Balloon(cdc.frame1)
        cdc.alterar_balao.bind_widget(cdc.alterar, balloonmsg="Clique para alterar as informações selecionadas.")

        cdc.apagar = Button(cdc.aba1,text='APAGAR', bd=2, bg='#B8860B', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.f_apagar)
        cdc.apagar.place(relx=0.415, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.apagar_balao = tix.Balloon(cdc.frame1)
        cdc.apagar_balao.bind_widget(cdc.apagar, balloonmsg="Clique para apagar as informações selecionadas.")

        cdc.buscar = Button(cdc.aba1, text='BUSCAR', bd=2, bg='#A52A2A', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.buscando)
        cdc.buscar.place(relx=0.725, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.buscar_balao = tix.Balloon(cdc.frame1)
        cdc.buscar_balao.bind_widget(cdc.buscar, balloonmsg='Clique para buscar as informações digitadas em "NOME DO CLIENTE".')

        cdc.limpar = Button(cdc.aba1,text='LIMPAR', bd=2, bg='#B8860B', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.limpando)
        cdc.limpar.place(relx=0.855, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.limpar_balao = tix.Balloon(cdc.frame1)
        cdc.limpar_balao.bind_widget(cdc.limpar, balloonmsg="Clique para limpar as informações digitadas.")

        # Entradas
        cdc.id_l = Label(cdc.aba1, text='ID', bg='#dfe3ee', fg='#800000')
        cdc.id_l.place(relx=0.0245, rely=0.05, relwidth=0.012, relheight=0.08)
        cdc.id_e = Entry(cdc.aba1)
        cdc.id_e.place(relx=0.025, rely=0.15, relwidth=0.06, relheight=0.08)

        cdc.dataM_l = Label(cdc.aba1, text='DATA DE MATRÍCULA', bg='#dfe3ee', fg='#800000')
        cdc.dataM_l.place(relx=0.11, rely=0.05, relwidth=0.1225, relheight=0.08)
        cdc.diaM_e = Entry(cdc.aba1)
        cdc.diaM_e.place(relx=0.1105, rely=0.15, relwidth=0.04, relheight=0.08)
        cdc.mesM_e = Entry(cdc.aba1)
        cdc.mesM_e.place(relx=0.155, rely=0.15, relwidth=0.04, relheight=0.08)
        cdc.anoM_e = Entry(cdc.aba1)
        cdc.anoM_e.place(relx=0.2, rely=0.15, relwidth=0.0525, relheight=0.08)

        cdc.nome_l = Label(cdc.aba1, text='NOME DO CLIENTE', bg='#dfe3ee', fg='#800000')
        cdc.nome_l.place(relx=0.276, rely=0.05, relwidth=0.1125, relheight=0.08)
        cdc.nome_e = Entry(cdc.aba1)
        cdc.nome_e.place(relx=0.277, rely=0.15, relwidth=0.7, relheight=0.08)

        cdc.rua_l = Label(cdc.aba1, text='RUA', bg='#dfe3ee', fg='#800000')
        cdc.rua_l.place(relx=0.025, rely=0.30, relwidth=0.025, relheight=0.08)
        cdc.rua_e = Entry(cdc.aba1)
        cdc.rua_e.place(relx=0.025, rely=0.40, relwidth=0.35, relheight=0.08)

        cdc.num_l = Label(cdc.aba1, text='NÚMERO', bg='#dfe3ee', fg='#800000')
        cdc.num_l.place(relx=0.4, rely=0.30, relwidth=0.055, relheight=0.08)
        cdc.num_e = Entry(cdc.aba1)
        cdc.num_e.place(relx=0.4, rely=0.40, relwidth=0.2, relheight=0.08)

        cdc.bairro_l = Label(cdc.aba1, text='BAIRRO', bg='#dfe3ee', fg='#800000')
        cdc.bairro_l.place(relx=0.625, rely=0.30, relwidth=0.045, relheight=0.08)
        cdc.bairro_e = Entry(cdc.aba1)
        cdc.bairro_e.place(relx=0.625, rely=0.40, relwidth=0.35, relheight=0.08)

        cdc.tel_l = Label(cdc.aba1, text='TELEFONE', bg='#dfe3ee', fg='#800000')
        cdc.tel_l.place(relx=0.025, rely=0.55, relwidth=0.055, relheight=0.08)
        cdc.tel_e = Entry(cdc.aba1)
        cdc.tel_e.place(relx=0.025, rely=0.65, relwidth=0.33, relheight=0.08)

        cdc.sexo_l = Label(cdc.aba1, text='SEXO', bg='#dfe3ee', fg='#800000')
        cdc.sexo_l.place(relx=0.387, rely=0.55, relwidth=0.032, relheight=0.08)
        cdc.sexo_V = StringVar()
        cdc.sexo_V.set('')
        cdc.sexo_c = OptionMenu(cdc.aba1, cdc.sexo_V, *('Masculino', 'Feminino'))
        cdc.sexo_c.place(relx=0.387, rely=0.64, relwidth=0.1, relheight=0.1)

        cdc.dataV_l = Label(cdc.aba1, text='DATA DE VENCIMENTO', bg='#dfe3ee', fg='#800000')
        cdc.dataV_l.place(relx=0.515, rely=0.55, relwidth=0.13, relheight=0.08)
        cdc.diaV_e = Entry(cdc.aba1)
        cdc.diaV_e.place(relx=0.515, rely=0.65, relwidth=0.04, relheight=0.08)
        cdc.mesV_e = Entry(cdc.aba1)
        cdc.mesV_e.place(relx=0.560, rely=0.65, relwidth=0.04, relheight=0.08)
        cdc.anoV_e = Entry(cdc.aba1)
        cdc.anoV_e.place(relx=0.605, rely=0.65, relwidth=0.0525, relheight=0.08)

        cdc.idade_l = Label(cdc.aba1, text='IDADE', bg='#dfe3ee', fg='#800000')
        cdc.idade_l.place(relx=0.685, rely=0.55, relwidth=0.037, relheight=0.08)
        cdc.idade_e = Entry(cdc.aba1)
        cdc.idade_e.place(relx=0.685, rely=0.65, relwidth=0.08, relheight=0.08)

        cdc.peso_l = Label(cdc.aba1, text='PESO', bg='#dfe3ee', fg='#800000')
        cdc.peso_l.place(relx=0.79, rely=0.55, relwidth=0.03, relheight=0.08)
        cdc.peso_e = Entry(cdc.aba1)
        cdc.peso_e.place(relx=0.79, rely=0.65, relwidth=0.08, relheight=0.08)

        cdc.altura_l = Label(cdc.aba1, text='ALTURA', bg='#dfe3ee', fg='#800000')
        cdc.altura_l.place(relx=0.895, rely=0.55, relwidth=0.05, relheight=0.08)
        cdc.altura_e = Entry(cdc.aba1)
        cdc.altura_e.place(relx=0.895, rely=0.65, relwidth=0.08, relheight=0.08)

    def aba2_f(cdc):
        # - ABA 2 -
        
        # Informações
        cdc.id_d1 = Label(cdc.aba2, text='ID', bg='#dfe3ee', fg='#800000')
        cdc.id_d1.place(relx=0.0245, rely=0.05, relwidth=0.012, relheight=0.08)
        cdc.id_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.id_d2.place(relx=0.025, rely=0.15, relwidth=0.06, relheight=0.08)

        cdc.dataM_d1 = Label(cdc.aba2, text='DATA DE MATRÍCULA', bg='#dfe3ee', fg='#800000')
        cdc.dataM_d1.place(relx=0.11, rely=0.05, relwidth=0.1225, relheight=0.08)
        cdc.diaM_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.diaM_d2.place(relx=0.1105, rely=0.15, relwidth=0.04, relheight=0.08)
        cdc.mesM_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.mesM_d2.place(relx=0.155, rely=0.15, relwidth=0.04, relheight=0.08)
        cdc.anoM_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.anoM_d2.place(relx=0.2, rely=0.15, relwidth=0.0525, relheight=0.08)

        cdc.nome_d1 = Label(cdc.aba2, text='NOME DO CLIENTE', bg='#dfe3ee', fg='#800000')
        cdc.nome_d1.place(relx=0.276, rely=0.05, relwidth=0.1125, relheight=0.08)
        cdc.nome_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.nome_d2.place(relx=0.277, rely=0.15, relwidth=0.7, relheight=0.08)

        cdc.rua_d1 = Label(cdc.aba2, text='RUA', bg='#dfe3ee', fg='#800000')
        cdc.rua_d1.place(relx=0.025, rely=0.30, relwidth=0.025, relheight=0.08)
        cdc.rua_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.rua_d2.place(relx=0.025, rely=0.40, relwidth=0.35, relheight=0.08)

        cdc.num_d1 = Label(cdc.aba2, text='NÚMERO', bg='#dfe3ee', fg='#800000')
        cdc.num_d1.place(relx=0.4, rely=0.30, relwidth=0.055, relheight=0.08)
        cdc.num_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.num_d2.place(relx=0.4, rely=0.40, relwidth=0.2, relheight=0.08)

        cdc.bairro_d1 = Label(cdc.aba2, text='BAIRRO', bg='#dfe3ee', fg='#800000')
        cdc.bairro_d1.place(relx=0.625, rely=0.30, relwidth=0.045, relheight=0.08)
        cdc.bairro_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.bairro_d2.place(relx=0.625, rely=0.40, relwidth=0.35, relheight=0.08)

        cdc.tel_d1 = Label(cdc.aba2, text='TELEFONE', bg='#dfe3ee', fg='#800000')
        cdc.tel_d1.place(relx=0.025, rely=0.55, relwidth=0.055, relheight=0.08)
        cdc.tel_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.tel_d2.place(relx=0.025, rely=0.65, relwidth=0.33, relheight=0.08)

        cdc.sexo_d1 = Label(cdc.aba2, text='SEXO', bg='#dfe3ee', fg='#800000')
        cdc.sexo_d1.place(relx=0.387, rely=0.55, relwidth=0.032, relheight=0.08)
        cdc.sexo_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.sexo_d2.place(relx=0.387, rely=0.65, relwidth=0.1, relheight=0.08)

        cdc.dataV_d1 = Label(cdc.aba2, text='DATA DE VENCIMENTO', bg='#dfe3ee', fg='#800000')
        cdc.dataV_d1.place(relx=0.515, rely=0.55, relwidth=0.13, relheight=0.08)
        cdc.diaV_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.diaV_d2.place(relx=0.515, rely=0.65, relwidth=0.04, relheight=0.08)
        cdc.mesV_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.mesV_d2.place(relx=0.560, rely=0.65, relwidth=0.04, relheight=0.08)
        cdc.anoV_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.anoV_d2.place(relx=0.605, rely=0.65, relwidth=0.0525, relheight=0.08)

        cdc.idade_d1 = Label(cdc.aba2, text='IDADE', bg='#dfe3ee', fg='#800000')
        cdc.idade_d1.place(relx=0.685, rely=0.55, relwidth=0.037, relheight=0.08)
        cdc.idade_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.idade_d2.place(relx=0.685, rely=0.65, relwidth=0.08, relheight=0.08)

        cdc.peso_d1 = Label(cdc.aba2, text='PESO', bg='#dfe3ee', fg='#800000')
        cdc.peso_d1.place(relx=0.79, rely=0.55, relwidth=0.03, relheight=0.08)
        cdc.peso_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.peso_d2.place(relx=0.79, rely=0.65, relwidth=0.08, relheight=0.08)

        cdc.altura_d1 = Label(cdc.aba2, text='ALTURA', bg='#dfe3ee', fg='#800000')
        cdc.altura_d1.place(relx=0.895, rely=0.55, relwidth=0.05, relheight=0.08)
        cdc.altura_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.altura_d2.place(relx=0.895, rely=0.65, relwidth=0.08, relheight=0.08)

        cdc.situacao_d1 = Label(cdc.aba2, text='SITUAÇÃO', bg='#dfe3ee', fg='#800000')
        cdc.situacao_d1.place(relx=0.025, rely=0.835, relwidth=0.06, relheight=0.08)
        cdc.situacao_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.situacao_d2.place(relx=0.1, rely=0.835, relwidth=0.11, relheight=0.08)

        cdc.di_at_d1 = Label(cdc.aba2, text='DIAS EM ATRASO', bg='#dfe3ee', fg='#800000')
        cdc.di_at_d1.place(relx=0.24, rely=0.835, relwidth=0.096, relheight=0.08)
        cdc.di_at_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.di_at_d2.place(relx=0.355, rely=0.835, relwidth=0.08, relheight=0.08)

        cdc.tmb_d1 = Label(cdc.aba2, text='GASTO CALÓRICO', bg='#dfe3ee', fg='#800000')
        cdc.tmb_d1.place(relx=0.46, rely=0.835, relwidth=0.105, relheight=0.08)
        cdc.tmb_d2 = Label(cdc.aba2, text="", bg='white', fg='black', relief='sunken')
        cdc.tmb_d2.place(relx=0.585, rely=0.835, relwidth=0.08, relheight=0.08)

        # Botões
        cdc.informacoes = Button(cdc.aba2, text='INFORMAÇÕES', bd=2, bg='#A52A2A', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.inf_dados)
        cdc.informacoes.place(relx=0.725, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.informacoes_balao = tix.Balloon(cdc.frame1)
        cdc.informacoes_balao.bind_widget(cdc.informacoes, balloonmsg='Clique para obter as informações selecionadas.')

        cdc.limpar = Button(cdc.aba2,text='LIMPAR', bd=2, bg='#B8860B', fg='white',
                            font=('calibri corpo', 8, 'bold'), command=cdc.limpando)
        cdc.limpar.place(relx=0.855, rely=0.82, relwidth=0.12, relheight=0.1)
        cdc.limpar_balao = tix.Balloon(cdc.frame1)
        cdc.limpar_balao.bind_widget(cdc.limpar, balloonmsg="Clique para limpar as informações digitadas.")

    def apps_f2(cdc):
        # Lista da Tela
        cdc.lista_c = ttk.Treeview(cdc.frame2, height=3, column=('col1','col2','col3','col4'))
        cdc.lista_c.heading('#0', text='')
        cdc.lista_c.heading('#1', text='ID')
        cdc.lista_c.heading('#2', text='Nome do Cliente')
        cdc.lista_c.heading('#3', text='Telefone')
        cdc.lista_c.heading('#4', text='Situação')

        cdc.lista_c.column('#0', width=0)
        cdc.lista_c.column('#1', width=50)
        cdc.lista_c.column('#2', width=300)
        cdc.lista_c.column('#3', width=200)
        cdc.lista_c.column('#4', width=200)

        cdc.lista_c.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # Barra de Scroll
        cdc.lista_c_scroll = Scrollbar(cdc.frame2, orient='vertical')
        cdc.lista_c.configure(yscroll=cdc.lista_c_scroll.set)
        cdc.lista_c_scroll.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

    def manual(cdc):
        # Funções
        cdc.root2 = Toplevel()
        cdc.root2.title("Manual de Uso")
        cdc.root2.configure(background='white')
        cdc.root2.geometry('300x850')
        cdc.root2.resizable(False, False)
        cdc.root2.transient(cdc.root)
        cdc.root2.focus_force() #Forçar o foco nesta janela quando Aberta
        cdc.root2.grab_set() #Impedir de digitar em outra janela quado esta estiver Aberta

        # Mensagem
        cdc.msg = Label(cdc.root2, text='''
        - Opções -  
        
        Sair: Fecha o programa.  
        
        - Limpar: 
        Limpa as informações digitadas
        na aba "Registro".  
         
         - Sobre -  
         
         - Manual: 
         Abre o manual de uso.  
        
        - Abas -  
        
        - Registro: 
        Aba para registro e pesquisa
        dos clientes da tabela.  
         
        - Dados: 
        Aba para visualização de dados
        do cliente selecionado na tabela.  
        
        - Botões -  
        
        - Salvar: 
        Salva as informações digitadas da
        aba "Registro" na tabela.  
         
        - Editar: 
        Retorna as informações do cliente
        selecionado na tabela para a aba 
        "Registro".  
         
        - Alterar: 
        Altera as informações digitadas na
        aba "Registro", pelas do cliente 
        selecionado na tabela.  
         
        - Apagar: 
        Apaga as informações do cliente 
        selecionado na tabela.  
        
        - Buscar: 
        Retorna na tabela o nome dos clientes 
        digitado em "NOME DO CLIENTE".
        Para retornar toda a tabela, basta 
        buscar com a caixa de diálogo do "NOME
        DO CLIENTE" vazia.
          
        - Informações: 
        Expõe as informações do cliente 
        na aba "Dados" selecinado na tabela.
        ''', bg='#dfe3ee', fg='black', relief='groove')
        cdc.msg.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

programa()

'''

Algorítmo inspirado na série de vídeos do professor Rafael de Leon.

Link da série de vídeos (18/06/2021): https://www.youtube.com/watch?v=RtrZcoVD1WM&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-

'''
