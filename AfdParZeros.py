#questão 2 da lista

class AfdParZeros: 
    def __init__(self):
        self.estado_atual = "q0" #Estado inicial
        
    def transicao(self, char):
        if self.estado_atual == "q0":
            if char == "0":
                self.estado_atual = "q1"
            elif char == "1":
                self.estado_atual = "q0"
        elif self.estado_atual == "q1":
            if char == "0":
                self.estado_atual = "q0"
            elif char == "1":
                self.estado_atual = "q1"
    
    def reconhece(self, string):
        self.estado_atual = 'q0'
    
        for char in string:
            self.transicao(char)
            
        return self.estado_atual == "q0"

afd = AfdParZeros()

#Teste
strings = ['1010', '110011', '000', '111', '010101']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' possui número par de zeros? {resultado}")
