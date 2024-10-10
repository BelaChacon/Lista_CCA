#questão 18 da lista

class AfdImpar:
    
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial
        self.estado_aceitacao = {'q1', 'q2', 'q3'}  
      
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1'  
            elif char == '1':
                self.estado_atual = 'q2'  
        elif self.estado_atual == 'q1':
            if char == '0':
                self.estado_atual = 'q0' 
            elif char == '1':
                self.estado_atual = 'q3' 
        elif self.estado_atual == 'q2':
            if char == '0':
                self.estado_atual = 'q3'  
            elif char == '1':
                self.estado_atual = 'q0
        elif self.estado_atual == 'q3':
            if char == '0':
                self.estado_atual = 'q2'  
            elif char == '1':
                self.estado_atual = 'q1' 

    def reconhece(self, string):
        self.estado_atual = 'q0' 
        for char in string:
            self.transicao(char) 
        
        return self.estado_atual in self.estado_aceitacao  

afd = AfdImpar()

#Teste
strings = ['0', '1', '01', '10', '0001', '1110', '101010', '000', '1111', '1100']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' possui número ímpar de '0's e '1's? {resultado}")
