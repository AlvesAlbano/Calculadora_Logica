import tkinter,ttg

class tabela(tkinter.Tk):
    entradas = []
    expressao = ""
    
    def __init__(self):
        super().__init__()

        self.title("tabela")
        self.display_texto = tkinter.StringVar()
        self.display_texto.set("")
        
        display = tkinter.Label(self,textvariable=self.display_texto)
        display.pack()
        
        A_btn = tkinter.Button(self,text="A",command=self.letra_A)
        A_btn.pack()
        B_btn = tkinter.Button(self,text="B",command=self.letra_B)
        B_btn.pack()
        AND_btn = tkinter.Button(self,text="∧",command=self.operador_AND)
        AND_btn.pack()
        resultado_btn = tkinter.Button(self,text="=",command=self.resultado)
        resultado_btn.pack()
    
    def letra_A(self):
        self.display_texto.set(self.display_texto.get() + "A")
        self.entradas.append("A")
        self.expressao += "A "
    def letra_B(self):
        self.display_texto.set(self.display_texto.get() + "B")
        self.entradas.append("B")
        self.expressao += "B "

    def operador_AND(self):
        self.display_texto.set(self.display_texto.get() + "∧")
        self.expressao += "and "

    def resultado(self):
        print(self.expressao,self.entradas)
        print(ttg.Truths(self.entradas,[self.expressao],ints=False))

fds = tabela()
fds.mainloop()