#questão 19 da lista

class AfnSubstring010:
    def __init__(self):
        self.estado_atual = 'q0'
        self.estado_aceitacao = 'q3' 
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1' 
            elif char == '1':
                self.estado_atual = 'q0' 
        elif self.estado_atual == 'q1':
            if char == '0':
                self.estado_atual = 'q1' 
            elif char == '1':
                self.estado_atual = 'q2'  
        elif self.estado_atual == 'q2':
            if char == '0':
                self.estado_atual = 'q3'  
            elif char == '1':
                self.estado_atual = 'q0'  

    def reconhece(self, string):
        self.estado_atual = 'q0'  
        for char in string:
            self.transicao(char)  
        
        return self.estado_atual == self.estado_aceitacao or self.estado_atual == 'q3'  

afn = AfnSubstring010()

#Teste
strings = ['010', '110', '1010', '000', '011010', '101110', '111111', '0001010', '00100', '10101']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' contém a substring '010'? {resultado}")
