from tkinter import *

def taxaOcupacao():
    global valor, valor02, janela_TO, botao_info_TO
    janela_TO = Tk()
    janela_TO.configure(bg = 'white')
    janela_TO.title('ArqCalc')
    janela_TO.resizable(False, False)
    
    label_intro02 = Label(janela_TO, width = 40, text = 'Olá, digite as informações abaixo.', font = 'Arial 12', bg = 'Grey', fg = 'white')
    label_intro02.grid(row = 0, column = 0)
    label_lote = Label(janela_TO, font = 'Arial 12', width = 40, text = 'tamanho do lote(m²)')
    label_lote.grid(row = 1)
    valor = Entry(janela_TO, width = 35, font = 'Arial 12')
    valor.grid(row = 2, column = 0)
    label_AC = Label(janela_TO, width = 40, font = 'Arial 12', text = 'Tamanho da área construída(m²)')
    label_AC.grid(row = 4)
    valor02 = Entry(janela_TO, width = 35, font = 'Arial 12')
    valor02.grid(row = 5, column = 0)
    botao_submit = Button(janela_TO, bg = 'grey', fg = 'white', text = 'aplicar', command = click01, font = 'Arial 12')
    botao_submit.grid(row = 7, column = 0)
    botao_reseta_TO = Button(janela_TO, bg = 'grey', fg = 'white', text = 'Resetar', font = 'Arial 12', command = resetarTO)
    botao_reseta_TO.grid(row = 8)
    botao_info_TO = Button(janela_TO, bg = 'grey', height = 1, fg = 'white', text = '...', font = 'Arial 12', command = infoTO)
    botao_info_TO.grid(row = 8, column = 1)

def indiceAproveitamento():
    global valor03, valor04, janela_IA
    janela_IA = Tk()
    janela_IA.configure(bg = 'white')
    janela_IA.title('ArqCalc')
    janela_IA.resizable(False, False)

    label_intro03 = Label(janela_IA, width = 40, text = 'Olá, digite as informações abaixo.', font = 'Arial 12', bg = 'Grey', fg = 'white')
    label_intro03.grid(row = 0, column = 0)
    label_ACT = Label(janela_IA, font = 'Arial 12', width = 40, text = 'tamanho do lote(m²)')
    label_ACT.grid(row = 1)
    valor03 = Entry(janela_IA, width = 35, font = 'Arial 12')
    valor03.grid(row = 2, column = 0)
    label_lote = Label(janela_IA, width = 40, font = 'Arial 12', text = 'Tamanho da área construída total(m²)')
    label_lote.grid(row = 4)
    valor04 = Entry(janela_IA, width = 35, font = 'Arial 12')
    valor04.grid(row = 5, column = 0)
    botao_submit02 = Button(janela_IA, bg = 'grey', fg = 'white', text = 'aplicar', command = click02, font = 'Arial 12')
    botao_submit02.grid(row = 7, column = 0)
    botao_reseta_IA = Button(janela_IA, bg = 'grey', fg = 'white', text = 'Resetar', font = 'Arial 12', command = resetarIA)
    botao_reseta_IA.grid(row = 8)
    botao_info_IA = Button(janela_IA, bg = 'grey', height = 1, fg = 'white', text = '...', font = 'Arial 12', command = infoIA)
    botao_info_IA.grid(row = 8, column = 1)

def areaPermeavel():
    global valor05, valor06, janela_AP
    janela_AP = Tk()
    janela_AP.configure(bg = 'white')
    janela_AP.title('ArqCalc')
    janela_AP.resizable(False, False)

    label_intro04 = Label(janela_AP, width = 40, text = 'Olá, digite as informações abaixo.', font = 'Arial 12', bg = 'Grey', fg = 'white')
    label_intro04.grid(row = 0, column = 0)
    label_perm = Label(janela_AP, font = 'Arial 12', width = 40, text = 'tamanho do lote(m²)')
    label_perm.grid(row = 1)
    valor05 = Entry(janela_AP, width = 35, font = 'Arial 12')
    valor05.grid(row = 2, column = 0)
    label_AP = Label(janela_AP, width = 40, font = 'Arial 12', text = 'Tamanho da área permeável(m²)')
    label_AP.grid(row = 4)
    valor06 = Entry(janela_AP, width = 35, font = 'Arial 12')
    valor06.grid(row = 5, column = 0)
    botao_submit03 = Button(janela_AP, bg = 'grey', fg = 'white', text = 'aplicar', command = click03, font = 'Arial 12')
    botao_submit03.grid(row = 7, column = 0)
    botao_reseta_AP = Button(janela_AP, bg = 'grey', fg = 'white', text = 'Resetar', font = 'Arial 12', command = resetarAP)
    botao_reseta_AP.grid(row = 8)

def del_infoTO():
    label_info.destroy()
    label_info_titulo.destroy()
    botao_voltar.destroy()

def infoTO():
    global label_info, label_info_titulo, botao_voltar
    text_info = 'A taxa de\n ocupação se\n refere a porcentagem\n que a área\n construída ocupa\n em relação\n ao lote'
    label_info_titulo = Label(janela_TO, font = 'arial 13', fg = 'white', bg = 'grey', text = 'ÁREA CONSTRUÍDA(DEFINIÇÃO)')
    label_info_titulo.grid(row = 1, column = 2)
    label_info = Label(janela_TO, font = 'arial 12', fg = 'black', text = text_info)
    label_info.grid(row = 4, column = 2)
    botao_voltar = Button(janela_TO, bg = 'grey', fg = 'white', text = 'Fechar', font = 'arial 12', command = del_infoTO)
    botao_voltar.grid(row = 8, column = 2)

def del_infoIA():
    label_info01.destroy()
    label_info_titulo01.destroy()
    botao_voltar01.destroy()

def infoIA():
    global label_info01, label_info_titulo01, botao_voltar01
    text_info01 = 'O índice de\n aproveitamento é\n a razão entre\na área construída\n total e a\n área total do lote'
    label_info_titulo01 = Label(janela_IA, font = 'arial 13', fg = 'white', bg = 'grey', text = 'ÍNDICE DE APROV.(DEFINIÇÃO)')
    label_info_titulo01.grid(row = 1, column = 2)
    label_info01 = Label(janela_IA, font = 'arial 12', fg = 'black', text = text_info01)
    label_info01.grid(row = 4, column = 2)
    botao_voltar01 = Button(janela_IA, bg = 'grey', fg = 'white', text = 'Fechar', font = 'arial 12', command = del_infoIA)
    botao_voltar01.grid(row = 8, column = 2)

def resetarTO():
    valor.delete(0, END)
    valor02.delete(0, END)
    label_result.destroy()

def resetarIA():
    valor03.delete(0, END)
    valor04.delete(0, END)
    label_result02.destroy()

def resetarAP():
    valor05.delete(0, END)
    valor06.delete(0, END)
    label_result03.destroy()

def click01():
    global result02, result01, label_result
    result01 = valor.get()
    result01 = float(result01)
    result02 = valor02.get()
    result02 = float(result02)
    resultado_final = (result02/result01)*100
    resultado_final_resumo = round(resultado_final,2)
    label_result = Label(janela_TO, text = (resultado_final_resumo,'%'), font = 'arial 14')
    label_result.grid(row = 6, column = 0)

def click02():
    global result03, result04, label_result02
    result03 = valor03.get()
    result03 = float(result03)
    result04 = valor04.get()
    result04 = float(result04)
    resultado_final02 = (result04/result03)
    resultado_final_resumo02 = round(resultado_final02,2)
    label_result02 = Label(janela_IA, text = (resultado_final_resumo02), font = 'arial 14')
    label_result02.grid(row = 6)

def click03():
    global result05, result06, label_result03
    result05 = valor05.get()
    result05 = float(result05)
    result06 = valor06.get()
    result06 = float(result06)
    resultado_final03 = (result06/result05)*100
    resultado_final_resumo03 = round(resultado_final03,2)
    label_result03 = Label(janela_AP, text = (resultado_final_resumo03,'%'), font = 'arial 14')
    label_result03.grid(row = 6)

janela = Tk()
janela.title('ArqCalc')
janela.config(bg = 'white')
janela.resizable(False, False)

logo = PhotoImage(file = 'Ativo 3.png')

space = Label(janela, bg = 'white', width = 50, height = 1)
space.grid(row = 1, column = 0)

label_logo = Label(janela, image=logo).grid(row = 0, column = 0)
label_intro = Label(janela, height = 2, width = 50, text = 'Olá, qual opção você deseja acessar?', font = 'Arial 12', bg = 'grey', fg = 'white')
label_intro.grid(row = 1, column = 0)

botao_TO = Button(janela, text = 'Taxa de ocupação', fg = 'white', font = 'Arial 12', bg = 'grey', command = taxaOcupacao)
botao_TO.grid(row = 2, column = 0)

botao_IA = Button(janela, text = 'Índice de aproveitamento', fg = 'white', font = 'Arial 12', bg = 'grey', command = indiceAproveitamento)
botao_IA.grid(row = 3, column = 0)

botao_AP = Button(janela, text = 'Área permeável', fg = 'white', font = 'Arial 12', bg = 'grey', command = areaPermeavel)
botao_AP.grid(row = 4, column = 0)

label_insta = Label(janela, width = 57, text = 'Siga-nos no instagram: @arq.jvl | @studio.habitarq', font = 'Arial 10', bg = 'Black', fg = 'white')
label_insta.grid(row = 5, column = 0)

janela.mainloop()