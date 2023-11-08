from tkinter import *
from tkinter import ttk

cor1 = '#8292b5' # cinza
cor2 = '#2d2e2e' # preto
cor3 = '#000000' # preto
cor4 = '#f27222' # azul
cor5 = '#ffffff' # branco



janela = Tk()
janela.title('calculadora')
janela.geometry('220x318')
janela.config(bg=cor2)


frame_tela = Frame(janela, width=220, height=50, bg=cor1, )
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=220, height=300)
frame_corpo.grid(row=1, column=0)


#criando o leitor 
valor_texto = StringVar()


todos_valores = ''



def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    valor_texto.set(todos_valores)

#função para calculo


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
def limpar_tela():
    global todos_valores
    todos_valores =''
    valor_texto.set('')


app_label = Label(frame_tela, textvariable=valor_texto, width=14, height=2, padx=9, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor1, fg=cor5   )
app_label.place(x=0,y=0)

b_1 = Button(frame_corpo, command=limpar_tela, text= 'C', width=9, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=4, y =0)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('%'), text= '%', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=107, y =0)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('/'), text= '/', width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=159, y =0)

 #segunda linha

b_4 = Button(frame_corpo, command=lambda:entrar_valores('7'), text= '7', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=2, y =52)
b_5 = Button(frame_corpo, command=lambda:entrar_valores('8'), text= '8', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=54, y =52)
b_6 = Button(frame_corpo, command=lambda:entrar_valores('9'), text= '9', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=107, y =52)
b_7 = Button(frame_corpo, command=lambda:entrar_valores('*'), text= '*', width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=159, y =52)

#terceira linha

b_8 = Button(frame_corpo, command=lambda:entrar_valores('4'), text= '4', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=2, y =105)
b_9 = Button(frame_corpo, command=lambda:entrar_valores('5'), text= '5', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=54, y =105)
b_10 = Button(frame_corpo, command=lambda:entrar_valores('6'), text= '6', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=107, y =105)
b_11 = Button(frame_corpo, command=lambda:entrar_valores('+'), text= '+', width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=159, y =105)

#quarta linha

b_12 = Button(frame_corpo, command=lambda:entrar_valores('1'), text= '1', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=2, y =158)
b_13 = Button(frame_corpo, command=lambda:entrar_valores('2'), text= '2', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=54, y =158)
b_14 = Button(frame_corpo, command=lambda:entrar_valores('3'), text= '3', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=107, y =158)
b_15 = Button(frame_corpo, command=lambda:entrar_valores('-'), text= '-', width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=159, y =158)

#quarta linha

b_16 = Button(frame_corpo, command=lambda:entrar_valores('0'), text= '0', width=9, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=4, y =212)
b_17 = Button(frame_corpo, command=lambda:entrar_valores('.'), text= '.', width=4, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=107, y =212)
b_18 = Button(frame_corpo, command=calcular, text= '=', width=5, height=2, bg=cor4, fg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=159, y =212)






janela.mainloop()

