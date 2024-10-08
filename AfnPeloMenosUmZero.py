#questão 6 da lista

class AfnPeloMenosUmZero:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q1'}
        self.estado_atual = {self.estado_inicial}
    
    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0':
                if char == '0':
                    novos_estados.add('q1')  
                elif char == '1':
                    novos_estados.add('q0')  
            elif estado == 'q1':
                novos_estados.add('q1') 
        self.estado_atual = novos_estados
    
    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}
        for char in string:
            self.transicao(char)
        # Verifica se algum dos estados possíveis é um estado de aceitação
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)

afn = AfnPeloMenosUmZero()

#Teste
strings = ['1', '0', '11', '01', '10', '00', '111', '0101', '0001', '']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui pelo menos um zero?: {resultado}")
