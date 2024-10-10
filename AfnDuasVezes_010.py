#questão 24 da lista

class AfnDuasVezes_010:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q4'} 
        self.estado_atual = self.estado_inicial

    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '0':
                self.estado_atual = 'q1'
        elif self.estado_atual == 'q1':
            if char == '1':
                self.estado_atual = 'q2'
            elif char == '0':
                self.estado_atual = 'q1'  
        elif self.estado_atual == 'q2':
            if char == '0':
                self.estado_atual = 'q3'
            elif char == '1':
                self.estado_atual = 'q2' 
        elif self.estado_atual == 'q3':
            if char == '1':
                self.estado_atual = 'q2'  
            elif char == '0':
                self.estado_atual = 'q1'  
        elif self.estado_atual == 'q4':
            if char == '0':
                self.estado_atual = 'q1'
            elif char == '1':
                self.estado_atual = 'q2'

    def reconhece(self, string):
        self.estado_atual = self.estado_inicial
        encontrou_primeira = False

        for char in string:
            self.transicao(char)
            if self.estado_atual == 'q3':
                if encontrou_primeira:
                    self.estado_atual = 'q4'  
                else:
                    encontrou_primeira = True

        return self.estado_atual in self.estados_aceitacao

# Testando o AFD
afd = AfdDuasVezes_010()
strings = ['010010', '0101010', '0100010', '0010010', '101010', '010', '0010', '01001010']

for string in strings:
    resultado = afd.reconhece(string)
    print(f"A string '{string}' contém '010' pelo menos duas vezes? {resultado}")
