# questão 3 da lista

class AfdDoisUm: 
    def __init__(self):
        self.estado_atual = 'q0' #Estado inicial
        
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q0'
            elif char == '1':
                self.estado_atual = 'q1'
        elif self.estado_atual == 'q1':
            if char == '0':
                self.estado_atual = 'q1'
            elif char == '1':
                self.estado_atual = 'q2'
        elif self.estado_atual == 'q2':
            if char == '0':
                self.estado_atual = 'q2'
            elif char == '1':
                self.estado_atual = 'q3' #Estado de rejeição
        elif self.estado_atual == 'q3':
            self.estado_atual = 'q3'
            
    def reconhece(self, string):
        self.estado_atual = 'q0'
        
        for char in string:
            self.transicao(char)
            
        return self.estado_atual == 'q2'
    
afd = AfdDoisUm()    
    
#Teste
strings = ['1010', '1100', '111', '10001', '010', '11111']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' possui dois números 1? {resultado}")
