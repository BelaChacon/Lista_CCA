#questão 9 da lista

class AfdSequencia101:
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '1':
                self.estado_atual = 'q1'
        elif self.estado_atual == 'q1':
            if char == '0':
                self.estado_atual = 'q2'
        elif self.estado_atual == 'q2':
            if char == '1':
                self.estado_atual = 'q3' 
            else:  
                self.estado_atual = 'q0'  
        elif self.estado_atual == 'q3':
            pass  #Não precisa mudar o estado

    def reconhece(self, string):
        self.estado_atual = 'q0' 
        for char in string:
            self.transicao(char)
        return self.estado_atual == 'q3'

afd = AfdSequencia101()

#Teste
strings = ['101', '1101', '00101', '1001', '000', '111', '10101', '010101', '101010', '000101']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' contém uma sequênica 101? {resultado}")
