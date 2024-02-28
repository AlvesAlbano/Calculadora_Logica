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
        NOT_btn = tkinter.Button(self,text="~",command=self.operador_NOT)
        NOT_btn.pack()
        CONDICIONAL_btn = tkinter.Button(self,text="→",command=self.operador_CONDICIONAL)
        CONDICIONAL_btn.pack()

        parenteses_aberto_btn = tkinter.Button(self,text="(",command=self.parenteses_aberto)
        parenteses_aberto_btn.pack()
        parenteses_fechado_btn = tkinter.Button(self,text=")",command=self.parenteses_fechado)
        parenteses_fechado_btn.pack()
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
    def operador_NOT(self):
        self.display_texto.set(self.display_texto.get() + "~")
        self.expressao += "~"
    def operador_CONDICIONAL(self):
        self.display_texto.set(self.display_texto.get() + "→")
        self.expressao += " => "

    def parenteses_aberto(self):
        self.display_texto.set(self.display_texto.get() + "(")
        self.expressao += "("
    def parenteses_fechado(self):
        self.display_texto.set(self.display_texto.get() + ")")
        self.expressao += ")"

    def resultado(self):
        self.entradas = list(set(self.entradas))
        print(self.expressao,self.entradas) #'p and q and r', 'p or q or r', '(p or (~q)) => r'
        try:
            tabela_verdade = ttg.Truths(self.entradas,[self.expressao],ints=False)
            print(f'{tabela_verdade} {tabela_verdade.valuation()}')
        except:
            print('jshgfjshgdf')

fds = tabela()
fds.mainloop()