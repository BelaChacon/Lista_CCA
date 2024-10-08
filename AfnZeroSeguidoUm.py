#questão 10 da lista

class AfnZeroSeguidoUm:
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial
        self.estado_aceitacao = 'q2'  #Estado de aceitação  
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1'  
        elif self.estado_atual == 'q1':
            if char == '0':
                self.estado_atual = 'q1' 
            elif char == '1':
                self.estado_atual = 'q2'  
        elif self.estado_atual == 'q2':
            pass 

    def reconhece(self, string):
        self.estado_atual = 'q0'  
        for char in string:
            self.transicao(char)
            
        return self.estado_atual in self.estado_aceitacao

afn = AfnZeroSeguidoUm()

#Teste
strings = ['01', '001', '100', '0001', '110', '111', '000', '10', '011', '0101', '1001']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui um zero seguido de pelo menos um número 1? {resultado}")
