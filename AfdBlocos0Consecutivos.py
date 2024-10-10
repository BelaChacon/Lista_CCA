# questão 16 da lista 

class AfdBlocos0Consecutivos:
    
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial
        self.estados_aceitacao = {'q1', 'q2'} 
    
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
                self.estado_atual = 'q2' 
        elif self.estado_atual == 'q3':
            self.estado_atual = 'q3'  
            
    def reconhece(self, string):
        self.estado_atual = 'q0' 
        for char in string:
            self.transicao(char)
        return self.estado_atual in self.estados_aceitacao  
      
afd = AfdBlocos0Consecutivos()            

#Teste
strings = ['0', '00', '11', '001', '0110', '0101', '000111']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' possui blocos de 0 consecutivos? {resultado}")
