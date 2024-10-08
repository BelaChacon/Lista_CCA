#questão 7 da lista

class Afn01_10:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q5'}
        self.estado_atual = {self.estado_inicial}
    
    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0':
                if char == '0':
                    novos_estados.add('q1')  
            elif estado == 'q1':
                if char == '1':
                    novos_estados.add('q2')  
            elif estado == 'q2':
                if char in {'0', '1'}:
                    novos_estados.add('q2') 
                    novos_estados.add('q3') 
            elif estado == 'q3':
                if char == '1':
                    novos_estados.add('q4')  
                novos_estados.add('q3')  
            elif estado == 'q4':
                if char == '0':
                    novos_estados.add('q5') 
        self.estado_atual = novos_estados
    
    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}
        for char in string:
            self.transicao(char)
        
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)

afn = Afn01_10()

#Teste
strings = ['010', '0110', '0101', '1010', '01ab10', '011010', '0010', '01', '10']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui 01 no início e 10 no final? {resultado}")
