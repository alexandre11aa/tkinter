from tkinter import *
import math

tela = Tk()
tela.title("ELLUZ v1.0")
tela.geometry("800x600+350+70")
tela.resizable(0, 0)

# carregando todas as imagens

imagem_tela_inicial          = PhotoImage(file="assets/tela_inicial.png")
imagem_tela_curva_simples    = PhotoImage(file="assets/tela_curvas_simples.png")
imagem_tela_curva_transicao  = PhotoImage(file="assets/tela_curvas_com_transicao.png")
imagem_tela_superelevacao    = PhotoImage(file="assets/tela_superelevacao.png")
imagem_tela_superlargura     = PhotoImage(file="assets/tela_superlargura.png")
imagem_tela_curva_vertical   = PhotoImage(file="assets/tela_curva_vertical.png")
imagem_tela_suporte          = PhotoImage(file="assets/tela_suporte.png")

def tela_inicial():

    # tela de suporte
    def suporte():
        # apagando atributos da tela inicial
        lb_tela_inicial.destroy()
        btn_suporte.destroy()

        btn_curva_simples.destroy()
        btn_curva_transicao.destroy()
        btn_superelevacao.destroy()
        btn_superlargura.destroy()
        btn_curva_verticais.destroy()

        # inserindo atributos na tela de suporte
        lb_tela_suporte = Label(tela, image=imagem_tela_suporte)
        lb_tela_suporte.place(x=-2, y=0)

        btn_voltar = Button(tela, bg="#0EA15D", bd=0, text="VOLTAR", font="arial 10 bold", fg="white", width=9, command=lambda: tela_inicial())
        btn_voltar.place(x=50, y=556)

        btn_sair = Button(tela, bg="#0EA15D", bd=0, text="SAIR", font="arial 10 bold", fg="white", width=9, command=lambda: quit())
        btn_sair.place(x=674, y=556)

    # tela do cálculo de curvs simples
    def curvas_simples():

        # apagando atributos da tela inicial
        lb_tela_inicial.destroy()
        btn_suporte.destroy()

        # inserindo atributos na tela de curvas simples
        lb_tela_curva_simples = Label(tela, image= imagem_tela_curva_simples)
        lb_tela_curva_simples.place(x=-2, y=0)

        txt_vel_proj   = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_vel_proj.place(x=290, y=122)

        txt_super_max  = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_super_max.place(x=290, y=153)

        txt_raio_curv  = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_raio_curv.place(x=290, y=185)

        txt_ang_centr  = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_ang_centr.place(x=290, y=215)

        txt_ponto_curv = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_ponto_curv.place(x=290, y=246)

        # função que faz os cálculos
        def calc_curvas_simples():
            velocidade = float(txt_vel_proj.get())
            emax = float(txt_super_max.get())
            raio_c = float(txt_raio_curv.get())
            ac = float(txt_ang_centr.get())
            p_de_curv = float(txt_ponto_curv.get())

            velocidades = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
            c_de_atrito = [0.2, 0.18, 0.16, 0.15, 0.15, 0.14, 0.14, 0.13, 0.11]

            for i in range(9):
                if velocidades[i] >= velocidade:
                    n = i
                    break
                else:
                    n = 8

            f = velocidade * c_de_atrito[n] / velocidades[n]

            # Raio Mínimo de Curvatura
            raio_min = velocidade ** 2 / (127 * (emax + f))
            lb_raio_min["text"] = ("{:.3f}".format(raio_min))
            print("Raio Mínimo de Curvatura: %.3fm" % raio_min)

            # Tangente Externa
            tan_e = raio_c * math.tan((ac * math.pi / 180) / 2)
            lb_tan_e["text"] = ("{:.3f}".format(tan_e))
            print("Tangente Externa: %.3fm" % tan_e)

            # Desenvolvimento da Curva
            des_cur = raio_c * ac * math.pi / 180
            lb_des_cur["text"] = ("{:.3f}".format(des_cur))
            print("Desenvolvimento da Curva: %.3fm" % des_cur)

            # Grau da Curva

            if raio_c < 100:
                corda = 5
            elif raio_c >= 100 and raio_c < 600:
                corda = 10
            else:
                corda = 20

            g_c = 180 * corda / (raio_c * math.pi)
            lb_g_c["text"] = ("{:.3f}".format(g_c))
            print("Grau da Curva: %.3f°" % g_c)

            # Afastamento da Curva
            afas_e = tan_e * math.tan((ac * math.pi / 180) / 4)
            lb_afas_e["text"] = ("{:.3f}".format(afas_e))
            print("Afastamento da Curva: %.3fm" % afas_e)

            # Ponto de Intersecção das Tangentes
            p_i_tan = p_de_curv + tan_e
            lb_p_i_tan["text"] = ("{:.3f}".format(p_i_tan))
            print("Ponto de Intersecção das Tangentes: %.3fm" % p_i_tan)

            # Ponto de Tangência
            p_tang = p_de_curv + des_cur
            lb_p_tang["text"] = ("{:.3f}".format(p_tang))
            print("Ponto de Tangência: %.3fm" % p_tang)

        # labels com os valores

        lb_raio_min = Label(tela, font="arial 10", text="", bg="white", fg="black", width=12)
        lb_raio_min.place(x=290, y=325)
        lb_tan_e = Label(tela, font="arial 10", text="", bg="white", fg="black", width=12)
        lb_tan_e.place(x=290, y=357)
        lb_des_cur = Label(tela, font="arial 10", text="", bg="white", fg="black", width=12)
        lb_des_cur.place(x=290, y=388)
        lb_g_c = Label(tela, font="arial 10", text="", bg="white", fg="black", width=12)
        lb_g_c.place(x=290, y=419)
        lb_afas_e = Label(tela, font="arial 10", text="", bg="white", fg="black", width=12)
        lb_afas_e.place(x=290, y=450)
        lb_p_i_tan = Label(tela, font="arial 10", text="", bg="white", fg="black", width=12)
        lb_p_i_tan.place(x=290, y=481)
        lb_p_tang = Label(tela, font="arial 10", text="", bg="white", fg="black", width=12)
        lb_p_tang.place(x=290, y=512)

        btn_voltar = Button(tela, bg="#0EA15D", bd=0, text="Voltar", font="arial 10", fg="white", width=9, command=lambda: tela_inicial())
        btn_voltar.place(x=40, y=560)
        btn_calcular = Button(tela, bg="black", bd=0, text="Calcular", font="arial 10", fg="white", width=9, command=lambda: calc_curvas_simples())
        btn_calcular.place(x=204, y=285)
        btn_sair = Button(tela, bg="#0EA15D", bd=0, text="Sair", font="arial 10", fg="white", width=9, command=lambda: quit())
        btn_sair.place(x=684, y=560)

    def curva_com_transicao():

        # apagando atributos da tela inicial
        lb_tela_inicial.destroy()
        btn_suporte.destroy()

        # inserindo atributos na tela de curvas simples
        lb_tela_curva_transicao = Label(tela, image=imagem_tela_curva_transicao)
        lb_tela_curva_transicao.place(x=-2, y=0)

        txt_vel_proj = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_vel_proj.place(x=290, y=122)

        txt_super_max = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_super_max.place(x=290, y=153)

        txt_raio_curv = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_raio_curv.place(x=290, y=185)

        txt_ang_centr = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_ang_centr.place(x=290, y=215)

        txt_ponto_curv = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=14, justify=CENTER)
        txt_ponto_curv.place(x=290, y=246)

        # funções que faz os cálculos
        def calc_curvas_com_transicao():

            velocidade = float(txt_vel_proj.get())
            emax = float(txt_super_max.get())
            raio_c = float(txt_raio_curv.get())
            ac = float(txt_ang_centr.get())
            p_de_curv = float(txt_ponto_curv.get())

            velocidades = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
            c_de_atrito = [0.2, 0.18, 0.16, 0.15, 0.15, 0.14, 0.14, 0.13, 0.11]

            for i in range(9):
                if velocidades[i] >= velocidade:
                    n = i
                    break
                else:
                    n = 8

            f = velocidade * c_de_atrito[n] / velocidades[n]

            # Raio Mínimo
            raio_m = velocidade ** 2 / (127 * (emax + f))

            # Comprimento Mínimo
            if (2 / 3.6) * velocidade > 0.036 * velocidade ** 3 / raio_c:
                ls_min = (2 / 3.6) * velocidade
            else:
                ls_min = 0.036 * velocidade ** 3 / raio_c
                print("Comprimento Mínimo: %.2fm" % ls_min)
            lb_ls_min["text"] = ("{:.3f}".format(ls_min))

            # Comprimento Máximo
            ls_max = (ac * math.pi / 180) * raio_c
            print("Comprimento Máximo: %.2fm" % ls_max)
            lb_ls_max["text"] = ("{:.3f}".format(ls_max))

            # Comprimento Adotado
            ls_desej = ls_min * 3
            print("Comprimento Adotado: %.2fm" % ls_desej)
            lb_ls_desej["text"] = ("{:.3f}".format(ls_desej))

            # Ângulo Central do Trecho em Espiral
            ang_c_e = (ls_desej / (2 * raio_c)) * 180 / math.pi
            print("Ângulo Central do Trecho em Espiral: %.2f°" % ang_c_e)
            lb_ang_c_e["text"] = ("{:.3f}".format(ang_c_e))

            # Ângulo Central do Trecho Circular
            ang_c_c = ac - 2 * ang_c_e
            print("Ângulo Central do Trecho Circular: %.2f°" % ang_c_c)
            lb_ang_c_c["text"] = ("{:.3f}".format(ang_c_c))

            # Desenvolvimento do Trecho Circular
            des_circ = raio_c * ((ang_c_c * math.pi) / 180)
            print("Desenvolvimento do Trecho Circular: %.2fm" % des_circ)
            lb_des_circ["text"] = ("{:.3f}".format(des_circ))

            # Abscissa dos pontos SC e CS (XS)
            abss_sc_cs = ls_desej * (1 - (((ang_c_e * math.pi) / 180) ** 2 / 10) + (((ang_c_e * math.pi) / 180) ** 4 / 216))
            print("Abscissa dos pontos SC e CS (XS): %.2fm" % abss_sc_cs)
            lb_abss_sc_cs["text"] = ("{:.3f}".format(abss_sc_cs))

            # Ordenada dos pontos SC e CS (YS)
            orde_sc_cs = ls_desej * (((((ang_c_e * math.pi) / 180) / 3)) - (((ang_c_e * math.pi) / 180) ** 3 / 42))
            print("Ordenada dos pontos SC e CS (YS): %.2fm" % orde_sc_cs)
            lb_orde_sc_cs["text"] = ("{:.3f}".format(orde_sc_cs))

            # Abscissa do Centro O' (K)
            abss_cent = abss_sc_cs - raio_c * math.sin(ang_c_e * math.pi / 180)
            lb_abss_cent["text"] = ("{:.3f}".format(abss_cent))
            print("Abscissa do Centro O' (K): %.2fm" % abss_cent)

            # Afastamento da Curva Circular
            afast_circ = orde_sc_cs - raio_c * (1 - math.cos(ang_c_e * math.pi / 180))
            print("Afastamento da Curva Circular: %.2fm" % afast_circ)
            lb_afast_circ["text"] = ("{:.3f}".format(afast_circ))

            # Tangente Total
            tan_tot = abss_cent + ((raio_c + afast_circ) * math.tan((ac * math.pi / 180) / 2))
            lb_tan_tot["text"] = ("{:.3f}".format(tan_tot))
            print("Tangente Total: %.2fm" % tan_tot)

            # Distância de PI à Curva Circular
            dis_pi = ((raio_c + afast_circ) / math.cos((ac * math.pi / 180) / 2)) - raio_c
            lb_dis_pi["text"] = ("{:.3f}".format(dis_pi))
            print("Distância de PI à Curva Circular: %.2fm" % dis_pi)

            # Ponto de interseção das Tangentes (PI)
            p_i = p_de_curv + tan_tot
            lb_p_i["text"] = ("{:.3f}".format(p_i))
            print("Ponto de interseção das Tangentes: %.2fm" % p_i)

            # Estaca de início do trecho circular (SC)
            s_c = p_de_curv + ls_desej
            lb_s_c["text"] = ("{:.3f}".format(s_c))
            print("Estaca de início do trecho circular: %.2fm" % s_c)

            # Estaca de fim do trecho circular (CS)
            c_s = s_c + des_circ
            lb_c_s["text"] = ("{:.3f}".format(c_s))
            print("Estaca de fim do trecho circular: %.2fm" % c_s)

            # Estaca de fim da curva de concordância com transição (ST)
            s_t = c_s + ls_desej
            lb_s_t["text"] = ("{:.3f}".format(s_t))
            print("Estaca de fim da curva de concordância com transição: %.2fm" % s_t)

        lb_ls_min = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_ls_min.place(x=290, y=320)
        lb_ls_max = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_ls_max.place(x=290, y=348)
        lb_ls_desej = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_ls_desej.place(x=290, y=376)
        lb_ang_c_e = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_ang_c_e.place(x=290, y=404)
        lb_ang_c_c = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_ang_c_c.place(x=290, y=432)
        lb_des_circ = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_des_circ.place(x=290, y=460)
        lb_abss_sc_cs = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_abss_sc_cs.place(x=290, y=488)
        lb_orde_sc_cs = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_orde_sc_cs.place(x=290, y=516)

        lb_abss_cent = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_abss_cent.place(x=644, y=320)
        lb_afast_circ = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_afast_circ.place(x=644, y=348)
        lb_tan_tot = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_tan_tot.place(x=644, y=376)
        lb_dis_pi = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_dis_pi.place(x=644, y=404)
        lb_p_i = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_p_i.place(x=644, y=432)
        lb_s_c = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_s_c.place(x=644, y=460)
        lb_c_s = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_c_s.place(x=644, y=488)
        lb_s_t = Label(tela, font="arial 8", text="", bg="white", fg="black", width=16)
        lb_s_t.place(x=644, y=516)

        # botões comuns
        btn_voltar = Button(tela, bg="#0EA15D", bd=0, text="Voltar", font="arial 10", fg="white", width=9,
                            command=lambda: tela_inicial())
        btn_voltar.place(x=40, y=560)
        btn_calcular = Button(tela, bg="black", bd=0, text="Calcular", font="arial 10", fg="white", width=9,
                              command=lambda: calc_curvas_com_transicao())
        btn_calcular.place(x=204, y=283)
        btn_sair = Button(tela, bg="#0EA15D", bd=0, text="Sair", font="arial 10", fg="white", width=9,
                          command=lambda: quit())
        btn_sair.place(x=684, y=560)

    def superelevacao():

        # apagando atributos da tela inicial
        lb_tela_inicial.destroy()
        btn_suporte.destroy()

        # inserindo novos atributos
        lb_tela_superelevacao = Label(tela, image=imagem_tela_superelevacao)
        lb_tela_superelevacao.place(x=-2, y=0)

        txt_vel_proj = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=30, justify=CENTER)
        txt_vel_proj.place(x=58, y=150)

        txt_super_max = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=30, justify=CENTER)
        txt_super_max.place(x=58, y=227)

        txt_raio_curv = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=30, justify=CENTER)
        txt_raio_curv.place(x=58, y=305)

        # definindo a função que faz os cálculos
        def calc_superelevacao():

            velocidade = float(txt_vel_proj.get())
            emax = float(txt_super_max.get())
            raio_c = float(txt_raio_curv.get())

            velocidades = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
            c_de_atrito = [0.2, 0.18, 0.16, 0.15, 0.15, 0.14, 0.14, 0.13, 0.11]

            for i in range(9):
                if velocidades[i] >= velocidade:
                    n = i
                    break
                else:
                    n = 8

            f = velocidade * c_de_atrito[n] / velocidades[n]

            # Raio Mínimo

            raio_m = velocidade ** 2 / (127 * (emax + f))

            superelevacao = emax * 100 * ((2 * raio_m / raio_c) - (raio_m ** 2 / raio_c ** 2))
            lb_superelevacao["text"] = ("{:.3f}".format(superelevacao))
            print("Superelevação: %.2f por cento" % superelevacao)

        lb_superelevacao = Label(tela, font="arial 10", text="", bg="white", fg="black", width=26)
        lb_superelevacao.place(x=58, y=457)


        btn_voltar = Button(tela, bg="#0EA15D", bd=0, text="Voltar", font="arial 10", fg="white", width=9,
                            command=lambda: tela_inicial())
        btn_voltar.place(x=40, y=560)
        btn_calcular = Button(tela, bg="black", bd=0, text="Calcular", font="arial 10", fg="white", width=9,
                              command=lambda : calc_superelevacao())
        btn_calcular.place(x=120, y=374)
        btn_sair = Button(tela, bg="#0EA15D", bd=0, text="Sair", font="arial 10", fg="white", width=9,
                          command=lambda: quit())
        btn_sair.place(x=684, y=560)

    def superlargura():

        # apagando atributos da tela inicial
        lb_tela_inicial.destroy()
        btn_suporte.destroy()

        # inserindo novos atributos
        lb_tela_superlargura = Label(tela, image=imagem_tela_superlargura)
        lb_tela_superlargura.place(x=-2, y=0)

        txt_vel_proj = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=36, justify=CENTER)
        txt_vel_proj.place(x=58, y=140)

        txt_l_f_veic = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=36, justify=CENTER)
        txt_l_f_veic.place(x=58, y=185)

        txt_dist_eix = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=36, justify=CENTER)
        txt_dist_eix.place(x=58, y=230)

        txt_balan_di = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=36, justify=CENTER)
        txt_balan_di.place(x=58, y=275)

        txt_folg_lat = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=36, justify=CENTER)
        txt_folg_lat.place(x=58, y=320)

        txt_larg_bas = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=36, justify=CENTER)
        txt_larg_bas.place(x=58, y=367)

        txt_raio_c = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=36, justify=CENTER)
        txt_raio_c.place(x=58, y=412)

        # função que calcula a superlargura
        def calc_superlargura():
            velocidade = float(txt_vel_proj.get())
            l_f_veic = float(txt_l_f_veic.get())
            dist_eix= float(txt_dist_eix.get())
            balan_di = float(txt_balan_di.get())
            folg_lat = float(txt_folg_lat.get())
            larg_bas = float(txt_larg_bas.get())
            raio_c = float(txt_raio_c.get())

            superlargura = 2 * (l_f_veic + (dist_eix ** 2 / (2 * raio_c)) + folg_lat) + (raio_c ** 2 + balan_di * 2 * dist_eix) ** (1 / 2) + (
                                       velocidade / (10 * raio_c ** (1 / 2))) - raio_c - larg_bas
            lb_superlargura["text"] = ("{:.3f}".format(superlargura))
            print("Superlargura: %.2fm" % superlargura)

        lb_superlargura = Label(tela, font="arial 10", text="", bg="white", fg="black", width=31)
        lb_superlargura.place(x=59, y=510)

        btn_voltar = Button(tela, bg="#0EA15D", bd=0, text="Voltar", font="arial 10", fg="white", width=9,
                            command=lambda: tela_inicial())
        btn_voltar.place(x=40, y=560)
        btn_calcular = Button(tela, bg="black", bd=0, text="Calcular", font="arial 10", fg="white", width=9,
                              command=lambda: calc_superlargura())
        btn_calcular.place(x=139, y=449)
        btn_sair = Button(tela, bg="#0EA15D", bd=0, text="Sair", font="arial 10", fg="white", width=9,
                          command=lambda: quit())
        btn_sair.place(x=684, y=560)

    def curva_vertical():

        # apagando atributos da tela inicial
        lb_tela_inicial.destroy()
        btn_suporte.destroy()

        # inserindo atributos na tela de curvas simples
        lb_tela_curva_simples = Label(tela, image=imagem_tela_curva_vertical)
        lb_tela_curva_simples.place(x=-2, y=0)

        txt_v = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=16, justify=CENTER)
        txt_v.place(x=270, y=120)

        txt_epiv = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=16, justify=CENTER)
        txt_epiv.place(x=270, y=153)

        txt_cota_piv = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=16, justify=CENTER)
        txt_cota_piv.place(x=270, y=185)

        txt_i1 = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=16, justify=CENTER)
        txt_i1.place(x=620, y=120)

        txt_i2 = Entry(tela, bd=2, font="arial 10", bg="white", fg="black", width=16, justify=CENTER)
        txt_i2.place(x=620, y=153)

        def calc_curva_vertical():

            v = float(txt_v.get())
            epiv = float(txt_epiv.get())
            cota_piv = float(txt_cota_piv.get())
            i1 = float(txt_i1.get())
            i2 = float(txt_i2.get())



        btn_voltar = Button(tela, bg="#0EA15D", bd=0, text="Voltar", font="arial 10", fg="white", width=9,
                            command=lambda: tela_inicial())
        btn_voltar.place(x=40, y=560)
        btn_calcular = Button(tela, bg="black", bd=0, text="Calcular", font="arial 10", fg="white", width=9,
                              command=lambda:None)
        btn_calcular.place(x=467, y=184)
        btn_sair = Button(tela, bg="#0EA15D", bd=0, text="Sair", font="arial 10", fg="white", width=9,
                          command=lambda: calc_curva_vertical())
        btn_sair.place(x=684, y=560)


    # inserindo a imagem
    lb_tela_inicial = Label(tela, image=imagem_tela_inicial)
    lb_tela_inicial.place(x=-2, y=0)

    # inserindo os botões da tela de inicio/ posicao
    btn_curva_simples = Button(tela, bg="#0EA15D", bd= 0, text="Curva Simples", font="arial 11", fg="white", width=24, command=lambda: curvas_simples())
    btn_curva_simples.place(x=304, y=105)

    btn_curva_transicao = Button(tela, bg="#0EA15D", bd=0, text="Curva com Transição", font="arial 11", fg="white", width=24, command=lambda: curva_com_transicao())
    btn_curva_transicao.place(x=323, y=153)

    btn_superelevacao = Button(tela, bg="#0EA15D", bd=0, text="Superelevação", font="arial 11", fg="white", width=24, command=lambda: superelevacao())
    btn_superelevacao.place(x=332, y=201)

    btn_superlargura = Button(tela, bg="#0EA15D", bd=0, text="Superlargura", font="arial 11", fg="white", width=24, command=lambda: superlargura())
    btn_superlargura.place(x=323, y=249)

    btn_curva_verticais = Button(tela, bg="#0EA15D", bd=0, text="Curva Vertical", font="arial 11", fg="white", width=24, command=lambda: curva_vertical())
    btn_curva_verticais.place(x=303, y=297)

    btn_suporte = Button(tela, bg="#0EA15D", bd=0, text="Suporte", font="arial 10", fg="white", width=9, command= lambda: suporte())
    btn_suporte.place(x=40, y=560)

    btn_sair = Button(tela, bg="#0EA15D", bd=0, text="Sair", font="arial 10", fg="white", width=9, command= lambda: quit())
    btn_sair.place(x=684, y=560)

tela_inicial()
tela.mainloop()