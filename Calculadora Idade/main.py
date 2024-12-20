from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

# cores

cor1 = "#3b3b3b" # preto/leve
cor2 = "#333333" # preto/pasado
cor3 = "#ffffff" # branco
cor4 = "#ffa500" # laranja


# criando frames

frame_cima = Frame(janela, width=310, height=140, pady=0,padx=0,relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, pady=0,padx=0,relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

# criando labels para frame cima

l_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=3, relief='flat',anchor='center', font=('Ivi 15 bold'), bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, padx=0, relief='flat',anchor='center', font=('Arial 35 bold'), bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)

# criando labels para frame baixo

l_data_inicial = Label(frame_baixo, text='Data Inicial', height=1, padx=0, pady=0, relief='flat',anchor=NW, font=('Ivi 11 '), bg=cor1, fg=cor3)
l_data_inicial.place(x=40, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_patter='mm/dd/y', y=2021)
cal_1.place(x=180, y=30)

l_data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0, pady=0, relief='flat',anchor=NW, font=('Ivi 11 '), bg=cor1, fg=cor3)
l_data_nascimento.place(x=40, y=70)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_patter='mm/dd/y', y=2021)
cal_2.place(x=180, y=70)






janela.mainloop()