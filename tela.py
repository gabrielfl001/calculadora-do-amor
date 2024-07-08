from tkinter import *
from tkinter import Tk, ttk 
import random 

from PIL import Image, ImageTk
o0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#FF69B4"     #hotpink


janela = Tk()
janela.title("")
janela.geometry('410x400')
janela.configure(background=co8)
janela.resizable(width=FALSE, height=FALSE)

Style = ttk.Style(janela)
Style.theme_use('clam')

#frames 
frameCima = Frame(janela, width = 418, height = 200, bg = co8)
frameCima.grid(row=0, column = 0)

frameMeio = Frame(janela, width = 418, height = 200, bg = co8, relief ='solid')
frameMeio.grid(row=1, column = 0)

# logo
app_ = Label(frameCima, text = 'calculadora do amor', width = 400, padx = 5, anchor = NW, font = 'Fixedsys 20', bg=co8, fg=co1)
app_.place(x=0, y=0)

#função calcular amor

def calcularamor(): 
    #pegando nomes
    nome1= seunome.get()
    nome2= parceironome.get()
    st = "0123456789"
    digitos = 2 
    resultados = "".join(random.sample(st,digitos))
    resultado ['text'] = 'Porcentagem de amor '
    resultado1 ['text'] = nome1 + ' e ' + nome2
    resultado2 ['text'] = resultados + '%'

#função para escolher opções

def escolher():
    #variaveis globais 
    global app_img, app_love 
    
    escolha1 = selecionado1.get()
    escolha2 = selecionado2.get()

    if escolha1 == 'Homem' and escolha2 == "Mulher":
        imagem1 = 'straightrem.png'
        imagem2 = 'coraçãorem.png'
    
    elif escolha1 =='Homem' and escolha2 =='Homem':
        imagem1 = 'gayrem.png'
        imagem2 = 'coraçãorem.png'

    elif escolha1 =='Mulher' and escolha2 =='Homem':
        imagem1 = 'straightrem.png'
        imagem2 = 'coraçãorem.png'

    elif escolha1 =='Mulher' and escolha2 =='Mulher':
        imagem1 = 'lesbainrem.png'
        imagem2 = 'coraçãorem.png'

    else:
        print('selecione os genero')
        return



    #abrindo imagem
    app_img = Image.open(imagem1)
    app_img = app_img.resize((140,140))
    app_img = ImageTk.PhotoImage(app_img)
    app_logo['image'] = app_img



#abrindo imagem
app_img = Image.open('coraçãorem.png')
app_img = app_img.resize((140,140))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima,image = app_img , width = 900,compound=LEFT, padx = 5, anchor = NW, bg=co8, fg=co1)
app_logo.place(x=20, y=50)


#resultados 
resultado = Label(frameCima, text = '', width = 35, padx = 10, anchor = NW, font = 'Verdana 10', bg=co8, fg=o0)
resultado.place(x=170, y=70)

resultado1 = Label(frameCima, text = '', width = 17, padx = 10, anchor = CENTER, font = 'Verdana 12 bold', bg=co8, fg=o0)
resultado1.place(x=170, y=100)

resultado2 = Label(frameCima, text = '', width = 5, padx = 10, anchor = CENTER, font = 'Verdana 25 bold', bg=co8, fg=o0)
resultado2.place(x=210, y=140)

# frame meio 
nome = Label(frameMeio, text = 'nome', anchor = NW, font = 'Ivy 10 bold', bg=co8, fg=o0)
nome.place(x=6, y=15)

seunome = Entry(frameMeio, width=15, font=('Ivy 14'), justify='center', relief='solid') 
seunome.place(x=10, y=40)

selecionado1 = StringVar()
rad1 = Radiobutton(frameMeio,command=escolher, text='Homem', bg=co8, font=('Ivy 10'), value='Homem', variable=selecionado1).place(x=10, y=80)
rad2 = Radiobutton(frameMeio,command = escolher,  text='Mulher', bg=co8, font=('Ivy 10'), value='Mulher', variable=selecionado1).place(x=10, y=105)

linha = Label(frameMeio, width=1, height=10, anchor = NW, font= 'Verdana 1', bg=o0, fg=o0)
linha.place(x=190, y=40)
linha = Label(frameMeio, width=1, height=10, anchor = NW, font= 'Verdana 1', bg=o0, fg=o0)
linha.place(x=200, y=40)

nome = Label(frameMeio, text = 'nome do/a parceiro/a', anchor = NW, font = 'Ivy 10 bold', bg=co8, fg=o0)
nome.place(x=217, y=15)

parceironome = Entry(frameMeio, width=15, font=('Ivy 14'), justify='center', relief='solid') 
parceironome.place(x=220, y=40)

selecionado2 = StringVar()
rad3 = Radiobutton(frameMeio,command=escolher, text='Homem', bg=co8, font=('Ivy 10'), value='Homem', variable=selecionado2).place(x=220, y=80)
rad4 = Radiobutton(frameMeio,command=escolher, text='Mulher', bg=co8, font=('Ivy 10'), value='Mulher', variable=selecionado2).place(x=220, y=105)

#botão de calcular

app_love = Image.open('maorem.png')
app_love = app_love.resize((50,50))
app_love = ImageTk.PhotoImage(app_love)

botaocalcular = Button(frameMeio,command= calcularamor,image = app_love,compound=LEFT, text='calcular amor'.upper(),font=('Fixedsys 20') , bg=co8, fg=co1)
botaocalcular.place(x=10, y=140)

janela.mainloop()