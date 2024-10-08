#questão 12 da lista

class AfnSubstring110:
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial

    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '1':
                self.estado_atual = 'q1'  
        elif self.estado_atual == 'q1':
            if char == '1':
                self.estado_atual = 'q2'  
            elif char == '0':
                self.estado_atual = 'q0' 
        elif self.estado_atual == 'q2':
            if char == '0':
                self.estado_atual = 'q3'  
            elif char == '1':
                self.estado_atual = 'q2'
        elif self.estado_atual == 'q3':
            pass  # Não muda o estado

    def reconhece(self, string):
        self.estado_atual = 'q0' 
        for char in string:
            self.transicao(char)

        return self.estado_atual == 'q3'

afn = AfnSubstring110()

#Teste
strings = ['110', '101', '001', '1110', '0110', '000', '010101', '111110', '1000110']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui a sequência 110? {resultado}")
