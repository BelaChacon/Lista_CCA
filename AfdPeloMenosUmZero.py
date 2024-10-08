#questão 4 da lista

class AfdPeloMenosUmZero:
    def __init__(self):
        self.estado_atual = 'q0' #Estado inicial
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1'
            elif char >= '1':
                self.estado_atual = 'q0'
        elif self.estado_atual == 'q1':
                self.estado_atual ='q1'
                
    def reconhece(self, string):
        self.estado_atual = 'q0'
        
        for char in string:
            self.transicao(char)
            
        return self.estado_atual == 'q1'
    
afd = AfdPeloMenosUmZero()    

#Teste
strings = ['1010', '111', '000', '0111', '1', '']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' tem pelo menos um zero? {resultado}")    
