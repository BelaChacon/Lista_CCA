#questão 1 da lista
class Afd:
    def __init__(self):
        self.estado_atual = 'q0'  #Estado inicial do autômato
    
    #Define as transições de estado
    def transicao(self, simbolo):
        if self.estado_atual == 'q0':
            if simbolo == '1':
                self.estado_atual = 'q1'
        elif self.estado_atual == 'q1':
            if simbolo == '0':
                self.estado_atual = 'q0'
    
    #Analisa o conteudo de entrada e verifica se é aceita
    def reconhece(self, cadeia):
        self.estado_atual = 'q0'
        
        for simbolo in cadeia:
            if simbolo not in ['0', '1']:
                print(f"Símbolo inválido encontrado: {simbolo}")
                return False
            self.transicao(simbolo)
        
        #O autômato aceita a cadeia se termina no estado 'q1'
        return self.estado_atual == 'q1'
    
afd = Afd()

#Teste
cadeias = ['110', '101', '1000', '1111', '001', '000', '1', '0']

for cadeia in cadeias:
    if afd.reconhece(cadeia):
        print(f"A cadeia '{cadeia}' foi aceita.")
    else:
        print(f"A cadeia '{cadeia}' foi rejeitada.")
