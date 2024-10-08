#questão 6 da lista

class AfnPeloMenosUmZero:
    def __init__(self):
        self.estado_atual = 'q0'
        self.estados_aceitacao = {'q1'}
    
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1'
            elif char == '1':
                self.estado_atual = 'q0'
        elif self.estado_atual == 'q1':
            self.estado_atual = 'q1'

    
    def reconhece(self, string):
        self.estado_atual = 'q0'
        for char in string:
            self.transicao(char)

        return self.estado_atual in self.estados_aceitacao

afn = AfnPeloMenosUmZero()

#Teste
strings = ['1', '0', '11', '01', '10', '00', '111', '0101', '0001', '']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui pelo menos um zero?: {resultado}")
