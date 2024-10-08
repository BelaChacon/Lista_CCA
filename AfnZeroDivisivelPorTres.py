#questão 8 da lista 

class AfnZeroDivisivelPorTres:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0'}
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1'
            elif char == '1':
                self.estado_atual = 'q0'
        elif self.estado_atual == 'q1':
            if char == '0':
                self.estado_atual = 'q2'
            elif char == '1':
                self.estado_atual = 'q1'
        elif self.estado_atual == 'q2':
            if char == '0':
                self.estado_atual = 'q0'
            elif char == '1':
                self.estado_atual = 'q2'
    
    def reconhece(self, string):
        self.estado_atual = 'q0'
        for char in string:
            self.transicao(char)

        return self.estado_atual in self.estados_aceitacao

afn = AfnZeroDivisivelPorTres()

#Teste
strings = ['0', '00', '000', '0000', '00000', '000000', '010101', '001100', '10101', '000111']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui uma quantidade de zero divisivel por 3? {resultado}")
