#questão 1 da lista
class Afd:
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial do autômato
    
    #Define as transições de estado
    def transicao(self, char):
        if self.estado_atual == 'q0':
            if char == '1':
                self.estado_atual = 'q1'
        elif self.estado_atual == 'q1':
            if char == '0':
                self.estado_atual = 'q0'
    
    #Analisa o conteudo de entrada e verifica se é aceita
    def reconhece(self, string):
        self.estado_atual = 'q0'
        
        for char in string:
            if char not in ['0', '1']:
                print(f"Caractere inválido: {char}")
                return False
            self.transicao(char)
        
        #O autômato aceita a cadeia se termina no estado 'q1'
        return self.estado_atual == 'q1'
    
afd = Afd()

#Teste
strings = ['110', '101', '1000', '1111', '001', '000', '1', '0']

for string in strings:
    if afd.reconhece(string):
        print(f"A string '{string}' foi aceita.")
    else:
        print(f"A string '{string}' foi rejeitada.")
