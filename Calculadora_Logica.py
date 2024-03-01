import tkinter,ttg,pandas

class Calculadora_Logica(tkinter.Tk):
    entradas = []
    expressao = ""
    
    def __init__(self):        
        super().__init__()

        self.title("Calculadora Lógica")
        self.display_texto = tkinter.StringVar()
        self.display_texto.set("")
        
        self.display_resultado = tkinter.StringVar()
        self.display_resultado.set("")
        
        self.geometry("")
    
        display_expressao = tkinter.Label(self, textvariable=self.display_texto)
        display_expressao.grid(row=0, column=0, columnspan=9, padx=10, pady=10)

        display_tabela = tkinter.Label(self, textvariable=self.display_resultado)
        display_tabela.grid(row=2, column=1, columnspan=9, padx=10, pady=10)
        
        A_btn = tkinter.Button(self, text="A", command=self.letra_A)
        A_btn.grid(row=1, column=0, padx=5, pady=5)
        
        B_btn = tkinter.Button(self, text="B", command=self.letra_B)
        B_btn.grid(row=1, column=1, padx=5, pady=5)
        
        AND_btn = tkinter.Button(self, text="∧", command=self.operador_AND)
        AND_btn.grid(row=1, column=2, padx=5, pady=5)
        
        NOT_btn = tkinter.Button(self, text="~", command=self.operador_NOT)
        NOT_btn.grid(row=1, column=3, padx=5, pady=5)
        
        CONDICIONAL_btn = tkinter.Button(self, text="→", command=self.operador_CONDICIONAL)
        CONDICIONAL_btn.grid(row=1, column=4, padx=5, pady=5)

        BICONDICIONAL_btn = tkinter.Button(self, text="↔", command=self.operador_BICONDICIONAL)
        BICONDICIONAL_btn.grid(row=1, column=5, padx=5, pady=5)

        parenteses_aberto_btn = tkinter.Button(self, text="(", command=self.parenteses_aberto)
        parenteses_aberto_btn.grid(row=1, column=6, padx=5, pady=5)
        
        parenteses_fechado_btn = tkinter.Button(self, text=")", command=self.parenteses_fechado)
        parenteses_fechado_btn.grid(row=1, column=7, padx=5, pady=5)
        
        resultado_btn = tkinter.Button(self, text="=", command=self.resultado)
        resultado_btn.grid(row=1, column=8, padx=5, pady=5)
        
        apagar_btn = tkinter.Button(self, text="CE",fg="red", command=self.apagar)
        apagar_btn.grid(row=1, column=9, padx=5, pady=5)

    
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

    def operador_BICONDICIONAL(self):
        self.display_texto.set(self.display_texto.get() + "↔")
        self.expressao += " = "

    def parenteses_aberto(self):
        self.display_texto.set(self.display_texto.get() + "(")
        self.expressao += "("
        
    def parenteses_fechado(self):
        self.display_texto.set(self.display_texto.get() + ")")
        self.expressao += ")"
    
    def apagar(self):
        self.entradas = []
        self.expressao = ""
        self.display_texto.set("")
        self.display_resultado.set("")
        
    def resultado(self):
        self.entradas = list(set(self.entradas))
        print(self.expressao, self.entradas) #'p and q and r', 'p or q or r', '(p or (~q)) => r'
        try:
            tabela_verdade = ttg.Truths(self.entradas, [self.expressao], ints=False)
            self.display_resultado.set(f'{self.display_resultado.get() + str(tabela_verdade)} \n {self.expressao} é uma {tabela_verdade.valuation()}')
            print(f'{tabela_verdade} {tabela_verdade.valuation()}')
        except:
            print("Insira uma fórmula bem formulada")
            self.display_resultado.set("Insira uma fórmula bem formulada")


calculadora = Calculadora_Logica()
calculadora.mainloop()
