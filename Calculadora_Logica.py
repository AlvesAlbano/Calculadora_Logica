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
            
        display_expressao = tkinter.Label(self, textvariable=self.display_texto)
        display_expressao.grid(row=0, column=0, columnspan=9, padx=10, pady=10)

        display_tabela = tkinter.Label(self, textvariable=self.display_resultado)
        display_tabela.grid(row=2, column=1, columnspan=9, padx=10, pady=10)
        
        P_btn = tkinter.Button(self, text="P", command=self.letra_P)
        P_btn.grid(row=1, column=0, padx=5, pady=5)
        
        Q_btn = tkinter.Button(self, text="Q", command=self.letra_Q)
        Q_btn.grid(row=1, column=1, padx=5, pady=5)
        
        AND_btn = tkinter.Button(self, text="∧", command=self.operador_AND)
        AND_btn.grid(row=1, column=2, padx=5, pady=5)

        OR_btn = tkinter.Button(self, text="v", command=self.operador_OR)
        OR_btn.grid(row=1, column=3, padx=5, pady=5)
        
        NOT_btn = tkinter.Button(self, text="~", command=self.operador_NOT)
        NOT_btn.grid(row=1, column=4, padx=5, pady=5)
        
        CONDICIONAL_btn = tkinter.Button(self, text="→", command=self.operador_CONDICIONAL)
        CONDICIONAL_btn.grid(row=1, column=5, padx=5, pady=5)

        BICONDICIONAL_btn = tkinter.Button(self, text="↔", command=self.operador_BICONDICIONAL)
        BICONDICIONAL_btn.grid(row=1, column=6, padx=5, pady=5)

        parenteses_aberto_btn = tkinter.Button(self, text="(", command=self.parenteses_aberto)
        parenteses_aberto_btn.grid(row=1, column=7, padx=5, pady=5)
        
        parenteses_fechado_btn = tkinter.Button(self, text=")", command=self.parenteses_fechado)
        parenteses_fechado_btn.grid(row=1, column=8, padx=5, pady=5)
        
        resultado_btn = tkinter.Button(self, text="=", command=self.resultado)
        resultado_btn.grid(row=1, column=9, padx=5, pady=5)
        
        limpar_btn = tkinter.Button(self, text="CE",fg="red", command=self.limpar)
        limpar_btn.grid(row=1, column=10, padx=5, pady=5)

    
    def letra_P(self):
        self.display_texto.set(self.display_texto.get() + "P")
        self.entradas.append("P")
        self.expressao += "P "
        
    def letra_Q(self):
        self.display_texto.set(self.display_texto.get() + "Q")
        self.entradas.append("Q")
        self.expressao += "Q "

    def operador_AND(self):
        self.display_texto.set(self.display_texto.get() + "∧")
        self.expressao += "and "

    def operador_OR(self):
        self.display_texto.set(self.display_texto.get() + "v")
        self.expressao += "or "
        
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

    def dentro_do_parenteses(self,entrada):
        expressoes_parenteses = []
        contador = 0
        temp = ""
        for char in entrada:
            if char == '(':
                contador += 1
                if contador > 1:
                    temp += char
            elif char == ')':
                contador -= 1
                if contador == 0:
                    expressoes_parenteses.append(temp)
                    temp = ""
                else:
                    temp += char
            elif contador > 0:
                temp += char
        return expressoes_parenteses
    
    def limpar(self):
        self.entradas = []
        self.expressao = ""
        self.display_texto.set("")
        self.display_resultado.set("")

    def traducao(self,entrada):
        if entrada == "Tautology":
            return "Tautologia"
        elif entrada == "Contingency":
            return "Contigencia"
        elif entrada == "Contradiction":
            return "Contradição"

    def resultado(self):
        self.entradas = list(set(self.entradas))
        # entradas_aux = self.dentro_do_parenteses(self.expressao)
        print(self.expressao, self.entradas) #'p and q and r', 'p or q or r', '(p or (~q)) => r'
        try:
            tabela_verdade = ttg.Truths(self.entradas, [self.expressao], ints=False)
            self.display_resultado.set(f'{str(tabela_verdade)} \n {self.display_texto.get()} é uma {self.traducao(tabela_verdade.valuation())}')
            print(f'{tabela_verdade} {tabela_verdade.valuation()}')
        except:
            print("Insira uma fórmula bem formulada")
            self.display_resultado.set("Insira uma fórmula bem formulada")

calculadora = Calculadora_Logica()
calculadora.mainloop()