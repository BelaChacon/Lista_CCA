#questão 8 da lista 

class AfnZeroDivisivelPorTres:
    def __init__(self):
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q0'}
        self.estado_atual = {self.estado_inicial}
    
    def transicao(self, char):
        novos_estados = set()
        for estado in self.estado_atual:
            if estado == 'q0':
                if char == '0':
                    novos_estados.add('q1') 
                novos_estados.add('q0') 
            elif estado == 'q1':
                if char == '0':
                    novos_estados.add('q2') 
                novos_estados.add('q1') 
            elif estado == 'q2':
                if char == '0':
                    novos_estados.add('q0') 
                novos_estados.add('q2')  
        self.estado_atual = novos_estados
    
    def reconhece(self, string):
        self.estado_atual = {self.estado_inicial}
        for char in string:
            self.transicao(char)
        return any(estado in self.estados_aceitacao for estado in self.estado_atual)

afn = AfnZeroDivisivelPorTres()

#Teste
strings = ['0', '00', '000', '0000', '00000', '000000', '111', '010101', '001100', '10101', '000111']

for string in strings:
    resultado = afn.reconhece(string)
    print(f"A string '{string}' possui uma quantidade de zeros divisivel por três? {resultado}")
